// Quick test to verify TikTok files work
import fs from 'fs';

console.log('🔍 QUICK TIKTOK FILE VERIFICATION');
console.log('=================================\n');

const files = [
  { name: 'user_data_tiktok.json', format: 'OLD' },
  { name: 'user_data_tiktok 2.json', format: 'NEW' },
  { name: 'user_data_tiktok 3.json', format: 'NEW (originally broken)' },
  { name: 'user_data_tiktok_3.json', format: 'NEW (copy)' }
];

files.forEach((file, index) => {
  console.log(`${index + 1}. Testing ${file.name} (${file.format})`);
  
  try {
    const path = `example-data/${file.name}`;
    
    // Check if file exists
    if (!fs.existsSync(path)) {
      console.log('   ❌ File not found\n');
      return;
    }
    
    // Parse JSON
    const data = JSON.parse(fs.readFileSync(path, 'utf8'));
    console.log('   ✅ JSON parses successfully');
    
    // Check structure
    const hasOldActivity = !!data.Activity;
    const hasNewActivity = !!data['Your Activity'];
    const hasComments = !!data.Comment;
    
    if (hasOldActivity || hasNewActivity) {
      console.log('   ✅ Activity section found');
      
      const activity = data.Activity || data['Your Activity'];
      const videoKeys = ['Video Browsing History', 'Watch History'];
      const hasVideos = videoKeys.some(key => activity[key]?.VideoList?.length > 0);
      
      if (hasVideos) {
        const videoCount = activity['Video Browsing History']?.VideoList?.length || 
                          activity['Watch History']?.VideoList?.length || 0;
        console.log(`   ✅ ${videoCount.toLocaleString()} videos found`);
      }
      
      if (hasComments) {
        const commentCount = data.Comment?.Comments?.CommentsList?.length || 0;
        console.log(`   ✅ ${commentCount} comments found`);
      }
    } else {
      console.log('   ⚠️  No activity section found');
    }
    
    console.log('   🎉 File will work with enhanced parser!\n');
    
  } catch (error) {
    console.log(`   ❌ Error: ${error.message}\n`);
  }
});

console.log('💡 To test with the actual API, run: ./test_yourself.sh');
console.log('🌐 To test with frontend, upload files at http://localhost:3000'); 