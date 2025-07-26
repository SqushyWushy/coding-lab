import express from "express";
import multer from "multer";
import { generateGeminiSummary } from "../services/gemini.js";

const router = express.Router();

// Configure multer for file upload
const upload = multer({
  storage: multer.memoryStorage(),
  limits: {
    fileSize: 10 * 1024 * 1024, // 10MB limit
  },
  fileFilter: (req, file, cb) => {
    // Accept JSON files or files with .json extension
    if (file.mimetype === "application/json" || 
        file.originalname.endsWith('.json') ||
        file.mimetype === "text/plain") {
      cb(null, true);
    } else {
      cb(new Error("Only JSON files are allowed"), false);
    }
  },
});

// Parse TikTok data and extract comprehensive insights
function parseTikTokData(jsonData) {
  try {
    const activity = jsonData.Activity || {};
    
    // Calculate time spent estimates
    const videoList = activity["Video Browsing History"]?.VideoList || [];
    const avgWatchTime = 30; // seconds per TikTok
    const totalWatchTimeSeconds = videoList.length * avgWatchTime;
    const totalWatchTimeHours = totalWatchTimeSeconds / 3600;
    const totalWatchTimeDays = totalWatchTimeHours / 24;
    
    // Calculate scroll distance (1.5 inches per TikTok)
    const scrollDistanceInches = videoList.length * 1.5;
    const scrollDistanceFeet = scrollDistanceInches / 12;
    const scrollDistanceMiles = scrollDistanceFeet / 5280;
    
    // Analyze login patterns
    const loginHistory = activity["Login History"]?.LoginHistoryList || [];
    const loginDates = loginHistory.map(login => new Date(login.Date)).filter(date => !isNaN(date.getTime()));
    const loginHours = loginDates.map(date => date.getHours());
    const mostActiveHour = loginHours.reduce((acc, hour) => {
      acc[hour] = (acc[hour] || 0) + 1;
      return acc;
    }, {});
    const peakHour = Object.entries(mostActiveHour).sort((a, b) => b[1] - a[1])[0];
    
    // Analyze binge sessions and streaks
    const videoDates = videoList.map(video => new Date(video.Date)).filter(date => !isNaN(date.getTime()));
    const videosPerDay = videoDates.reduce((acc, date) => {
      const dayKey = date.toISOString().split('T')[0];
      acc[dayKey] = (acc[dayKey] || 0) + 1;
      return acc;
    }, {});
    const bingeDays = Object.entries(videosPerDay).filter(([day, count]) => count >= 100);
    
    // Find most active day
    const mostActiveDay = Object.entries(videosPerDay).sort((a, b) => b[1] - a[1])[0];
    
    // Calculate longest streak (consecutive days with activity)
    const sortedDays = Object.keys(videosPerDay).sort();
    let currentStreak = 1;
    let longestStreak = 1;
    let longestStreakStart = sortedDays[0];
    let currentStreakStart = sortedDays[0];
    
    for (let i = 1; i < sortedDays.length; i++) {
      const currentDate = new Date(sortedDays[i]);
      const prevDate = new Date(sortedDays[i - 1]);
      const dayDiff = Math.floor((currentDate - prevDate) / (1000 * 60 * 60 * 24));
      
      if (dayDiff === 1) {
        currentStreak++;
        if (currentStreak > longestStreak) {
          longestStreak = currentStreak;
          longestStreakStart = currentStreakStart;
        }
      } else {
        currentStreak = 1;
        currentStreakStart = sortedDays[i];
      }
    }
    
    const longestStreakEnd = new Date(longestStreakStart);
    longestStreakEnd.setDate(longestStreakEnd.getDate() + longestStreak - 1);
    
    // Analyze search patterns
    const searchHistory = activity["Search History"]?.SearchList || [];
    const searchTerms = searchHistory.map(search => search.SearchTerm.toLowerCase());
    const searchFrequency = searchTerms.reduce((acc, term) => {
      acc[term] = (acc[term] || 0) + 1;
      return acc;
    }, {});
    const topSearches = Object.entries(searchFrequency)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10);
    
    // Analyze comment patterns and personality FIRST (before yearly analysis)
    const comments = jsonData.Comment?.Comments || {};
    const commentList = comments.CommentsList || [];
    const commentCount = commentList.length;
    
    // Extract comment text and dates for personality analysis
    const commentTexts = commentList.map(comment => comment.comment || '').filter(text => text.length > 0);
    const commentDates = commentList.map(comment => new Date(comment.date)).filter(date => !isNaN(date.getTime()));
    
    // Extract longest comments with metadata
    const commentsWithMetadata = commentList.map(comment => ({
      text: comment.comment || '',
      length: (comment.comment || '').length,
      date: comment.date
    })).filter(comment => comment.text.length > 0);
    
    const longestComments = commentsWithMetadata
      .sort((a, b) => b.length - a.length)
      .slice(0, 10);

    // Extract hashtags from comments
    const hashtagPattern = /#[a-zA-Z0-9_]+/g;
    const allHashtags = [];
    commentTexts.forEach(text => {
      const hashtags = text.match(hashtagPattern);
      if (hashtags) {
        allHashtags.push(...hashtags.map(tag => tag.substring(1).toLowerCase()));
      }
    });
    
    const hashtagFrequency = allHashtags.reduce((acc, tag) => {
      acc[tag] = (acc[tag] || 0) + 1;
      return acc;
    }, {});
    
    const topHashtags = Object.entries(hashtagFrequency)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([tag, count]) => ({ tag, count }));

    // Analyze comment sentiment and patterns
    const commentAnalysis = {
      totalComments: commentCount,
      averageCommentLength: commentTexts.length > 0 ? 
        (commentTexts.reduce((sum, text) => sum + text.length, 0) / commentTexts.length).toFixed(1) : 0,
      shortComments: commentTexts.filter(text => text.length <= 10).length,
      longComments: commentTexts.filter(text => text.length > 50).length,
      emojiUsage: commentTexts.filter(text => /[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F1E0}-\u{1F1FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]/u.test(text)).length,
      questionComments: commentTexts.filter(text => text.includes('?')).length,
      exclamationComments: commentTexts.filter(text => text.includes('!')).length,
      longestComments: longestComments,
      topCommentWords: commentTexts.length > 0 ? 
        commentTexts.join(' ').toLowerCase()
          .replace(/[^\w\s]/g, '')
          .split(/\s+/)
          .filter(word => word.length > 3)
          .reduce((acc, word) => {
            acc[word] = (acc[word] || 0) + 1;
            return acc;
          }, {}) : {}
    };
    
    // Year-by-year analysis
    const yearlyAnalysis = {};
    const allActivityDates = [
      ...videoDates,
      ...searchHistory.map(search => new Date(search.Date)).filter(date => !isNaN(date.getTime())),
      ...commentDates || [],
      ...loginHistory.map(login => new Date(login.Date)).filter(date => !isNaN(date.getTime()))
    ].filter(date => !isNaN(date.getTime()));
    
    allActivityDates.forEach(date => {
      const year = date.getFullYear();
      if (!yearlyAnalysis[year]) {
        yearlyAnalysis[year] = {
          videos: 0,
          searches: 0,
          comments: 0,
          logins: 0,
          totalActivity: 0
        };
      }
      yearlyAnalysis[year].totalActivity++;
    });
    
    // Count videos by year
    videoDates.forEach(date => {
      const year = date.getFullYear();
      if (yearlyAnalysis[year]) {
        yearlyAnalysis[year].videos++;
      }
    });
    
    // Count searches by year
    searchHistory.forEach(search => {
      const date = new Date(search.Date);
      if (!isNaN(date.getTime())) {
        const year = date.getFullYear();
        if (yearlyAnalysis[year]) {
          yearlyAnalysis[year].searches++;
        }
      }
    });
    
    // Count comments by year
    if (commentDates) {
      commentDates.forEach(date => {
        const year = date.getFullYear();
        if (yearlyAnalysis[year]) {
          yearlyAnalysis[year].comments++;
        }
      });
    }
    
    // Count logins by year
    loginHistory.forEach(login => {
      const date = new Date(login.Date);
      if (!isNaN(date.getTime())) {
        const year = date.getFullYear();
        if (yearlyAnalysis[year]) {
          yearlyAnalysis[year].logins++;
        }
      }
    });
    

    
    // Sort years and get top activity year
    const sortedYears = Object.entries(yearlyAnalysis)
      .sort((a, b) => b[1].totalActivity - a[1].totalActivity);
    const mostActiveYear = sortedYears[0];

    // Activity over time (monthly breakdown)
    const activityOverTime = {};
    videoDates.forEach(date => {
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (!activityOverTime[monthKey]) {
        activityOverTime[monthKey] = {
          videos: 0,
          searches: 0,
          comments: 0,
          logins: 0
        };
      }
      activityOverTime[monthKey].videos++;
    });

    // Daily activity heatmap data
    const dailyActivity = {};
    videoDates.forEach(date => {
      const dateKey = date.toISOString().split('T')[0]; // YYYY-MM-DD
      dailyActivity[dateKey] = (dailyActivity[dateKey] || 0) + 1;
    });

    // Hourly activity pattern
    const hourlyActivity = Array(24).fill(0);
    videoDates.forEach(date => {
      hourlyActivity[date.getHours()]++;
    });

    // Login hours for activity clock
    const loginHourlyPattern = Array(24).fill(0);
    loginHistory.forEach(login => {
      const hour = new Date(login.Date).getHours();
      loginHourlyPattern[hour]++;
    });

    // Weekly patterns
    const weeklyActivity = Array(7).fill(0); // Sunday = 0, Monday = 1, etc.
    videoDates.forEach(date => {
      weeklyActivity[date.getDay()]++;
    });



    searchHistory.forEach(search => {
      const date = new Date(search.Date);
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (activityOverTime[monthKey]) {
        activityOverTime[monthKey].searches++;
      }
    });

    if (commentDates) {
      commentDates.forEach(date => {
        const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
        if (activityOverTime[monthKey]) {
          activityOverTime[monthKey].comments++;
        }
      });
    }

    loginHistory.forEach(login => {
      const date = new Date(login.Date);
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (activityOverTime[monthKey]) {
        activityOverTime[monthKey].logins++;
      }
    });
    
    // Analyze favorite sounds
    const favoriteSounds = activity["Favorite Sounds"]?.FavoriteSoundList || [];
    const soundFrequency = favoriteSounds.reduce((acc, sound) => {
      const soundId = sound.Link.split('/').pop();
      acc[soundId] = (acc[soundId] || 0) + 1;
      return acc;
    }, {});
    const topSounds = Object.entries(soundFrequency)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5);
    
    // Analyze social behavior
    const followers = activity["Follower List"]?.FansList || [];
    const following = activity["Following List"]?.Following || [];
    const likes = activity["Like List"]?.ItemFavoriteList || [];
    const shares = activity["Share History"]?.ShareHistoryList || [];
    
    // Analyze live streaming behavior
    const goLiveHistory = jsonData["Tiktok Live"]?.["Go Live History"] || {};
    const watchLiveHistory = jsonData["Tiktok Live"]?.["Watch Live History"] || {};
    const liveStreams = Object.keys(goLiveHistory).length;
    const liveWatches = Object.keys(watchLiveHistory).length;
    
    // Analyze shopping behavior
    const shoppingHistory = jsonData["Tiktok Shopping"] || {};
    const hasShoppingActivity = Object.keys(shoppingHistory).length > 0;
    
    // Analyze status updates
    const statusList = activity.Status?.["Status List"] || [];
    
    // Analyze video creation (if any)
    const videos = jsonData.Video?.Videos || {};
    const createdVideos = Object.keys(videos).length;
    
    // Engagement trends over time (after all variables are declared)
    const engagementTrends = {};
    
    // Videos trend
    videoDates.forEach(date => {
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (!engagementTrends[monthKey]) {
        engagementTrends[monthKey] = { videos: 0, likes: 0, comments: 0, searches: 0 };
      }
      engagementTrends[monthKey].videos++;
    });

    // Likes trend (if available)
    likes.forEach(like => {
      const date = new Date(like.Date);
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (engagementTrends[monthKey]) {
        engagementTrends[monthKey].likes++;
      }
    });

    // Search trend
    searchHistory.forEach(search => {
      const date = new Date(search.Date);
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      if (engagementTrends[monthKey]) {
        engagementTrends[monthKey].searches++;
      }
    });
    
    const insights = {
      // Core engagement metrics
      totalVideosWatched: videoList.length,
      totalLikes: likes.length,
      totalFavorites: activity["Favorite Videos"]?.FavoriteVideoList?.length || 0,
      totalShares: shares.length,
      totalComments: commentCount,
      
      // Time analysis
      totalWatchTime: {
        seconds: totalWatchTimeSeconds,
        hours: totalWatchTimeHours,
        days: totalWatchTimeDays
      },
      scrollDistance: {
        inches: scrollDistanceInches,
        feet: scrollDistanceFeet,
        miles: scrollDistanceMiles
      },
      
      // Social metrics
      followers: followers.length,
      following: following.length,
      socialRatio: following.length > 0 ? (followers.length / following.length).toFixed(2) : 0,
      
      // Activity patterns
      loginCount: loginHistory.length,
      peakActivityHour: peakHour ? { hour: parseInt(peakHour[0]), count: peakHour[1] } : null,
      bingeDays: {
        count: bingeDays.length,
        days: bingeDays.map(([day, count]) => ({ date: day, videos: count }))
      },
      mostActiveDay: mostActiveDay ? {
        date: mostActiveDay[0],
        videos: mostActiveDay[1]
      } : null,
      longestStreak: {
        days: longestStreak,
        startDate: longestStreakStart,
        endDate: longestStreakEnd.toISOString().split('T')[0]
      },
      
      // Content preferences
      favoriteVideos: {
        count: activity["Favorite Videos"]?.FavoriteVideoList?.length || 0,
        items: activity["Favorite Videos"]?.FavoriteVideoList || [],
        timeRange: null,
      },
      favoriteEffects: {
        count: activity["Favorite Effects"]?.FavoriteEffectsList?.length || 0,
        items: activity["Favorite Effects"]?.FavoriteEffectsList || [],
        timeRange: null,
      },
      favoriteSounds: {
        count: favoriteSounds.length,
        items: favoriteSounds,
        topSounds: topSounds,
        timeRange: null,
      },
      
      // Search behavior
      searchHistory: {
        count: searchHistory.length,
        items: searchHistory,
        topSearches: topSearches,
        uniqueTerms: Object.keys(searchFrequency).length
      },
      
      // Additional features
      liveStreaming: {
        streamsCreated: liveStreams,
        streamsWatched: liveWatches
      },
      shopping: {
        hasActivity: hasShoppingActivity,
        activityCount: Object.keys(shoppingHistory).length
      },
      statusUpdates: statusList.length,
      videosCreated: createdVideos,
      
      // Comment analysis
      comments: commentAnalysis,
      
      // Yearly analysis
      yearlyAnalysis: yearlyAnalysis,
      mostActiveYear: mostActiveYear ? {
        year: mostActiveYear[0],
        activity: mostActiveYear[1]
      } : null,
      
      // New detailed analysis
      hashtags: topHashtags,
      activityOverTime: activityOverTime,
      dailyActivity: dailyActivity,
      hourlyActivity: hourlyActivity,
      loginHourlyPattern: loginHourlyPattern,
      weeklyActivity: weeklyActivity,
      engagementTrends: engagementTrends,
      
      // Time ranges for all categories
      timeRanges: {}
    };

    // Calculate time ranges for all categories
    const allDates = [];
    
    // Collect dates from all sources
    if (insights.favoriteVideos.items.length > 0) {
      allDates.push(...insights.favoriteVideos.items.map(item => new Date(item.Date)));
    }
    if (insights.favoriteSounds.items.length > 0) {
      allDates.push(...insights.favoriteSounds.items.map(item => new Date(item.Date)));
    }
    if (insights.searchHistory.items.length > 0) {
      allDates.push(...insights.searchHistory.items.map(item => new Date(item.Date)));
    }
    if (loginHistory.length > 0) {
      allDates.push(...loginHistory.map(login => new Date(login.Date)));
    }
    
    // Calculate overall time range
    const validDates = allDates.filter(date => !isNaN(date.getTime())).sort((a, b) => a - b);
    if (validDates.length > 0) {
      insights.timeRanges = {
        earliest: validDates[0].toISOString(),
        latest: validDates[validDates.length - 1].toISOString(),
        span: Math.ceil((validDates[validDates.length - 1] - validDates[0]) / (1000 * 60 * 60 * 24)) // days
      };
    }
    
    // Calculate individual time ranges
    if (insights.favoriteVideos.items.length > 0) {
      const dates = insights.favoriteVideos.items
        .map(item => new Date(item.Date))
        .filter(date => !isNaN(date.getTime()))
        .sort((a, b) => a - b);
      
      if (dates.length > 0) {
        insights.favoriteVideos.timeRange = {
          earliest: dates[0].toISOString(),
          latest: dates[dates.length - 1].toISOString(),
          span: Math.ceil((dates[dates.length - 1] - dates[0]) / (1000 * 60 * 60 * 24))
        };
      }
    }
    
    if (insights.favoriteSounds.items.length > 0) {
      const dates = insights.favoriteSounds.items
        .map(item => new Date(item.Date))
        .filter(date => !isNaN(date.getTime()))
        .sort((a, b) => a - b);
      
      if (dates.length > 0) {
        insights.favoriteSounds.timeRange = {
          earliest: dates[0].toISOString(),
          latest: dates[dates.length - 1].toISOString(),
          span: Math.ceil((dates[dates.length - 1] - dates[0]) / (1000 * 60 * 60 * 24))
        };
      }
    }

    return insights;
  } catch (error) {
    throw new Error(`Failed to parse TikTok data: ${error.message}`);
  }
}

// Generate comprehensive AI prompt based on parsed data
function generateAnalysisPrompt(insights) {
  const prompt = `
🧠 **DEEP TIKTOK PERSONALITY ANALYSIS**

This user has been exposed! Here's their complete digital footprint:

📊 **CORE METRICS:**
- Videos Watched: ${insights.totalVideosWatched.toLocaleString()} TikToks
- Total Watch Time: ${insights.totalWatchTime.hours.toFixed(1)} hours (${insights.totalWatchTime.days.toFixed(1)} days!)
- Scroll Distance: ${insights.scrollDistance.miles.toFixed(2)} miles (${insights.scrollDistance.feet.toFixed(0)} feet)
- Likes Given: ${insights.totalLikes.toLocaleString()}
- Favorites Saved: ${insights.totalFavorites}
- Shares Made: ${insights.totalShares}
- Comments Posted: ${insights.totalComments}

👥 **SOCIAL BEHAVIOR:**
- Followers: ${insights.followers}
- Following: ${insights.following}
- Social Ratio: ${insights.socialRatio} (follower/following ratio)
- Videos Created: ${insights.videosCreated}
- Live Streams: ${insights.liveStreaming.streamsCreated} created, ${insights.liveStreaming.streamsWatched} watched

⏰ **ACTIVITY PATTERNS:**
- Login Count: ${insights.loginCount}
- Peak Activity Hour: ${insights.peakActivityHour ? `${insights.peakActivityHour.hour}:00 (${insights.peakActivityHour.count} logins)` : 'Unknown'}
- Binge Days: ${insights.bingeDays.count} days with 100+ videos watched
${insights.bingeDays.days.length > 0 ? `- Biggest Binge: ${insights.bingeDays.days[0]?.videos} videos on ${insights.bingeDays.days[0]?.date}` : ''}

🔍 **SEARCH BEHAVIOR:**
- Total Searches: ${insights.searchHistory.count}
- Unique Search Terms: ${insights.searchHistory.uniqueTerms}
- Top Searches: ${insights.searchHistory.topSearches.slice(0, 5).map(([term, count]) => `"${term}" (${count}x)`).join(', ')}

🎵 **CONTENT PREFERENCES:**
- Favorite Sounds: ${insights.favoriteSounds.count}
- Favorite Effects: ${insights.favoriteEffects.count}
- Top Sounds: ${insights.favoriteSounds.topSounds.slice(0, 3).map(([sound, count]) => `Sound ${sound} (${count}x)`).join(', ')}

💬 **COMMENT PERSONALITY:**
- Total Comments: ${insights.comments.totalComments}
- Average Comment Length: ${insights.comments.averageCommentLength} characters
- Emoji Usage: ${insights.comments.emojiUsage} comments with emojis
- Question Comments: ${insights.comments.questionComments}
- Exclamation Comments: ${insights.comments.exclamationComments}
- Top Comment Words: ${Object.entries(insights.comments.topCommentWords).slice(0, 5).map(([word, count]) => `"${word}" (${count}x)`).join(', ')}

📅 **STREAKS & PATTERNS:**
- Longest Streak: ${insights.longestStreak.days} consecutive days (${insights.longestStreak.startDate} to ${insights.longestStreak.endDate})
- Most Active Day: ${insights.mostActiveDay ? `${insights.mostActiveDay.videos} videos on ${insights.mostActiveDay.date}` : 'Unknown'}
- Most Active Year: ${insights.mostActiveYear ? `${insights.mostActiveYear.year} (${insights.mostActiveYear.activity.totalActivity} total activities)` : 'Unknown'}

🛒 **ADDITIONAL ACTIVITY:**
- Shopping Activity: ${insights.shopping.hasActivity ? 'Yes' : 'No'}
- Status Updates: ${insights.statusUpdates}

⏱️ **TIME SPAN:**
${insights.timeRanges.span ? `- Total Activity Span: ${insights.timeRanges.span} days (${(insights.timeRanges.span/365).toFixed(1)} years)` : ''}

---

**ANALYSIS REQUEST:**

Please provide a comprehensive, mildly confronting analysis that includes:

1. **Time Addiction Assessment**: How much of their life has been consumed by TikTok? (Use the watch time and scroll distance data)

2. **Personality Archetype**: What type of TikTok user are they? (Creator, Consumer, Lurker, Influencer, etc.)

3. **Comment Personality Analysis**: Based on their comment patterns, what type of person are they? Are they:
   - Philosophical/deep thinkers (long comments, existential questions)
   - Emoji-heavy expressives (lots of emojis, exclamations)
   - Short and sweet (brief comments, "fyp", etc.)
   - Question-askers (lots of "?" comments)
   - Supportive/encouraging (positive language patterns)
   - Controversial/troll-like (negative or provocative comments)

4. **Content Obsessions**: Based on search terms, favorites, and comment topics, what are their main interests/obsessions?

5. **Social Behavior Analysis**: Are they a social butterfly or a lurker? What does their follower/following ratio reveal?

6. **Binge Behavior & Streaks**: Analyze their binge days, longest streak, and peak activity hours - are they a night owl, early bird, or all-day scroller?

6. **Digital Wellness Score**: Rate their TikTok health from 1-10 based on usage patterns

7. **Year-by-Year Evolution**: What phases have they gone through? (e.g., "2021: Self-help phase, 2022: Astrology obsession, 2023: Fitness content") Use the yearly analysis data to show their evolution.

8. **Streak Analysis**: What does their longest streak reveal about their dedication? Are they consistent or sporadic users?

9. **Reality Check**: Give them a wake-up call about their usage - be honest but not mean

10. **Recommendations**: How can they have a healthier relationship with TikTok?

Make this analysis engaging, insightful, and slightly confronting. Use the data to tell a story about who this person is based on their digital behavior. Be specific with numbers and patterns. Keep it around 400-500 words.
`;

  return prompt;
}

// POST /analyze - Main analysis endpoint
router.post("/", upload.single("tiktokData"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ 
        error: "No file uploaded. Please upload a TikTok user_data.json file." 
      });
    }

    // Parse the uploaded JSON file
    let jsonData;
    try {
      jsonData = JSON.parse(req.file.buffer.toString());
    } catch (parseError) {
      return res.status(400).json({ 
        error: "Invalid JSON file. Please upload a valid TikTok user_data.json file." 
      });
    }

    // Parse TikTok data
    const insights = parseTikTokData(jsonData);
    
    // Generate AI analysis prompt
    const prompt = generateAnalysisPrompt(insights);
    
    // Get AI summary
    const aiSummary = await generateGeminiSummary(prompt);
    
    if (!aiSummary) {
      return res.status(500).json({ 
        error: "Failed to generate AI analysis. Please try again." 
      });
    }

    // Return comprehensive analysis results
    res.json({
      success: true,
      data: {
        insights,
        aiSummary,
        summary: {
          // Core metrics
          totalVideosWatched: insights.totalVideosWatched,
          totalWatchTime: insights.totalWatchTime,
          scrollDistance: insights.scrollDistance,
          totalLikes: insights.totalLikes,
          totalFavorites: insights.totalFavorites,
          totalShares: insights.totalShares,
          totalComments: insights.totalComments,
          
          // Social metrics
          followers: insights.followers,
          following: insights.following,
          socialRatio: insights.socialRatio,
          videosCreated: insights.videosCreated,
          
          // Activity patterns
          loginCount: insights.loginCount,
          peakActivityHour: insights.peakActivityHour,
          bingeDays: insights.bingeDays,
          mostActiveDay: insights.mostActiveDay,
          longestStreak: insights.longestStreak,
          
          // Content preferences
          favoriteVideos: insights.favoriteVideos.count,
          favoriteEffects: insights.favoriteEffects.count,
          favoriteSounds: insights.favoriteSounds.count,
          topSearches: insights.searchHistory.topSearches.slice(0, 5),
          
          // Additional features
          liveStreaming: insights.liveStreaming,
          shopping: insights.shopping,
          statusUpdates: insights.statusUpdates,
          
          // Comment analysis
          comments: insights.comments,
          
          // Yearly analysis
          yearlyAnalysis: insights.yearlyAnalysis,
          mostActiveYear: insights.mostActiveYear,
          
          // New detailed analysis
          hashtags: insights.hashtags,
          activityOverTime: insights.activityOverTime,
          dailyActivity: insights.dailyActivity,
          hourlyActivity: insights.hourlyActivity,
          loginHourlyPattern: insights.loginHourlyPattern,
          weeklyActivity: insights.weeklyActivity,
          engagementTrends: insights.engagementTrends,
          
          // Time analysis
          timeSpan: insights.timeRanges.span || "Unknown"
        }
      }
    });

  } catch (error) {
    console.error("Analysis error:", error);
    res.status(500).json({ 
      error: "Analysis failed. Please try again." 
    });
  }
});

export default router; 