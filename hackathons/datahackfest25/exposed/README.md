# ✨ EXPOSED

> **Your TikTok, Reflected Back At You - Transform Your Digital Data Into Beautiful Insights**

A premium, TikTok-style web application that transforms your TikTok data export into stunning data visualizations and AI-powered personality insights. Built for **Data Hackfest 2025** with modern design principles and cutting-edge technology.

![EXPOSED Preview](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![React](https://img.shields.io/badge/React-19-blue)
![Node.js](https://img.shields.io/badge/Node.js-23-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-blue)
![Gemini AI](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange)
![Auth0](https://img.shields.io/badge/Auth0-Secure-purple)

## 🌟 What Makes EXPOSED Special

**EXPOSED** is not just another data visualization tool - it's a **digital mirror** that reveals the hidden patterns, habits, and personality traits buried in your TikTok data. With stunning TikTok-style animations and comprehensive analysis, it turns boring data exports into meaningful self-discovery.

## 🎨 Key Features

### 🌈 **TikTok-Style Visual Experience**
- **Animated gradient titles** that flow with vibrant colors
- **Modern glassmorphism design** with backdrop blur effects
- **Smooth micro-interactions** and hover animations
- **Mobile-responsive** interface that works everywhere
- **Consistent TikTok aesthetic** throughout the entire app

### 📊 **Advanced Data Visualizations**
- **📅 Activity Heatmap** - GitHub-style contribution calendar showing daily TikTok usage
- **🕐 24-Hour Activity Clock** - Radial chart revealing your peak activity hours
- **📈 Engagement Trends** - Multi-line charts tracking videos, likes, comments over time
- **💬 Interactive Word Clouds** - Most frequently used words with hover effects
- **📊 Weekly Activity Patterns** - Weekday vs weekend usage comparison
- **📱 Monthly Usage Charts** - Historical activity trends with animated bars

### 🧠 **AI-Powered Insights**
- **Comprehensive personality analysis** using Google Gemini 2.0 Flash
- **Beautifully formatted markdown** with proper styling and readability
- **Digital behavior classification** (creator, consumer, lurker profiles)
- **Comment sentiment analysis** with emoji and pattern detection
- **Personalized wellness recommendations** based on usage patterns

### 🎯 **Comprehensive Data Analysis**
- **26,000+ video analysis** with detailed watch time calculations
- **Top 10 longest comments** with timestamps and character counts
- **Most frequently used hashtags** with usage statistics
- **Streak detection** for consecutive usage periods
- **Peak activity identification** with contextual insights
- **Social interaction patterns** (follower/following analysis)

### 🔐 **Secure & User-Friendly**
- **Custom Auth0 branding** that matches the app's aesthetic
- **Drag & drop file uploads** for seamless data import
- **Dynamic loading animations** with progress tracking and stage updates
- **Step-by-step data guide** for both technical and non-technical users
- **Privacy-first approach** - all data processed locally, never stored

### 📚 **Comprehensive User Experience**
- **Detailed onboarding guide** explaining how to get TikTok data
- **Troubleshooting sections** for common issues
- **Responsive help system** integrated throughout the app
- **Beautiful error handling** with helpful feedback

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- MongoDB Atlas account
- Google Gemini API key
- Auth0 account (optional - app works with demo mode)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd exposed
```

2. **Backend Setup**
```bash
cd backend
npm install
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

4. **Environment Configuration**

**Backend (.env)**
```bash
MONGODB_URI=your_mongodb_atlas_uri
GEMINI_API_KEY=your_gemini_api_key
PORT=4000
```

**Frontend (.env)**
```bash
VITE_AUTH0_DOMAIN=your-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id
VITE_AUTH0_CALLBACK_URL=http://localhost:5173
```

5. **Start the Application**
```bash
# Terminal 1 - Backend
cd backend
node app.js

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

6. **Access the Application**
- **Frontend**: `http://localhost:5173`
- **Backend**: `http://localhost:4000`

## 📊 Sample Analysis Results

Here's what EXPOSED discovered from a comprehensive TikTok export:

### 🎯 **Core Digital Footprint**
- **26,939 videos watched** (over 26K TikToks consumed!)
- **224.5 hours** of total watch time (9.4 full days!)
- **0.64 miles scrolled** (3,367 feet of finger movement!)
- **6,000 likes given** with social network of 68 followers, 3,980 following

### 💬 **Communication Patterns**
- **147 total comments** with 35.2 character average length
- **Top 10 longest comments** with detailed timestamps
- **Most used hashtags** with frequency analysis
- **Comment word cloud** revealing personality traits
- **Emotional expression patterns** through emoji usage

### 📅 **Activity Insights**
- **114-day longest streak** (July 24 - Nov 14, 2024)
- **Peak activity day**: 612 videos on September 2, 2024! 🤯
- **Weekly patterns**: Weekday vs weekend usage comparison
- **Hourly heatmap**: Peak activity hours throughout the day
- **Monthly trends**: Growth and decline patterns over time

### 🧭 **Digital Behavior Analysis**
- **Personality archetype** classification based on interaction patterns
- **Content preference mapping** through liked videos and searches
- **Social engagement score** calculated from comment/like ratios
- **Digital wellness recommendations** for healthier usage

## 🏗️ Technical Architecture

### **Frontend Stack**
- **React 19** with modern hooks and functional components
- **Vite** for lightning-fast development and building
- **Tailwind CSS** with custom animations and gradients
- **Auth0** for secure authentication with custom branding
- **Marked.js** for beautiful markdown rendering
- **Custom SVG visualizations** for charts and graphs

### **Backend Stack**
- **Node.js + Express** RESTful API architecture
- **MongoDB Atlas** for scalable data persistence
- **Google Gemini 2.0 Flash** for AI-powered analysis
- **Multer** for secure file upload handling
- **Comprehensive data parsers** for TikTok JSON exports

### **Data Processing Pipeline**
1. **Drag & Drop Upload** → File validation and JSON parsing
2. **Multi-Source Extraction** → Videos, comments, searches, likes, follows
3. **Advanced Analytics** → Streaks, patterns, frequencies, trends
4. **Visualization Preparation** → Data formatting for charts and graphs
5. **AI Enhancement** → Gemini analysis for personality insights
6. **Markdown Formatting** → Beautiful, readable AI summaries

## 🎨 Design Philosophy

### **TikTok-Inspired Aesthetic**
EXPOSED captures the energy and vibrancy of TikTok itself:
- **Flowing animated gradients** that never get boring
- **Vibrant color palettes** (coral, teal, sky blue, mint, yellow, purple)
- **Smooth transitions** and micro-animations everywhere
- **Modern typography** with perfect hierarchy and spacing
- **Glassmorphism effects** for depth and sophistication

### **Data Storytelling**
Every visualization tells a story:
- **Narrative-driven sections** that build understanding progressively
- **Contextual explanations** for every metric and insight
- **Emotional data presentation** that connects with users personally
- **Beautiful visual hierarchy** that guides attention naturally

### **Premium User Experience**
- **Intuitive interactions** with drag & drop, hover effects, and smooth animations
- **Comprehensive onboarding** with step-by-step guides for all skill levels
- **Responsive design** that works perfectly on mobile, tablet, and desktop
- **Accessibility considerations** with proper contrast and readable fonts

## 🔧 Advanced Features

### **Interactive Data Visualizations**
- **Activity Heatmap**: GitHub-style calendar with hover tooltips and intensity colors
- **24-Hour Clock**: Radial visualization showing peak usage hours with beautiful gradients
- **Engagement Trends**: Multi-line charts with interactive data points and legends
- **Word Clouds**: Dynamic sizing and positioning with click animations
- **Weekly Patterns**: Animated bar charts comparing weekday vs weekend activity

### **AI-Powered Analysis**
- **Personality Profiling**: Deep analysis of comment patterns and social behaviors
- **Digital Wellness Scoring**: Health recommendations based on usage patterns
- **Trend Identification**: AI detection of changes in behavior over time
- **Content Preference Mapping**: Understanding what content resonates with users
- **Social Network Analysis**: Insights into following/follower relationships

### **User Experience Enhancements**
- **Dynamic Loading States**: Beautiful progress bars with stage-by-stage updates
- **Comprehensive Error Handling**: Helpful messages and recovery suggestions
- **Mobile-First Design**: Perfect experience on any device size
- **Custom Auth0 Integration**: Branded login experience that matches the app
- **Privacy Assurance**: Clear messaging about data handling and security

## 🛡️ Privacy & Security

- **Local Processing**: All analysis happens in your browser/device
- **Zero Data Storage**: No personal information stored permanently
- **Auth0 Security**: Enterprise-grade authentication and authorization
- **Secure File Handling**: Validated uploads with proper error handling
- **Transparent Processing**: Clear explanations of what data is analyzed

## 📱 Responsive Design

EXPOSED works beautifully across all devices:
- **Mobile**: Touch-optimized interface with swipe gestures
- **Tablet**: Perfect layout for both portrait and landscape
- **Desktop**: Full-featured experience with hover states and animations
- **Large Screens**: Optimized spacing and typography for 4K+ displays

## 🚀 Deployment Guide

### **Production Backend**
```bash
# Set production environment variables
export MONGODB_URI=your_production_mongodb_uri
export GEMINI_API_KEY=your_gemini_api_key
export PORT=process.env.PORT || 4000

# Start production server
node app.js
```

### **Production Frontend**
```bash
# Build optimized production bundle
npm run build

# Deploy to Vercel, Netlify, or your preferred platform
# Update Auth0 settings for production domain
```

### **Environment Configuration**
- **Auth0**: Configure production domains and callback URLs
- **MongoDB**: Set up production cluster with proper security
- **Gemini API**: Configure rate limiting and usage monitoring
- **CORS**: Update allowed origins for production domains

## 🎯 Hackathon Highlights

**EXPOSED** was built for **Data Hackfest 2025** and showcases:

### **🏆 Innovation**
- **Novel data visualization approach** combining multiple chart types
- **TikTok-style UI/UX** bringing social media aesthetics to data analysis
- **AI-powered personality insights** that go beyond basic metrics
- **Custom Auth0 branding** for seamless user experience

### **🔧 Technical Excellence**
- **Modern full-stack architecture** with React 19 and Node.js
- **Advanced data processing** handling complex TikTok export formats
- **Custom visualization components** built from scratch with SVG and Canvas
- **Responsive design** that works flawlessly across all devices

### **🎨 User Experience**
- **Intuitive onboarding** with comprehensive guides for all users
- **Beautiful animations** that enhance rather than distract
- **Accessibility considerations** ensuring everyone can use the app
- **Privacy-first approach** building user trust and confidence

### **📊 Data Impact**
- **Meaningful insights** that help users understand their digital habits
- **Actionable recommendations** for digital wellness and behavior change
- **Beautiful storytelling** that makes data analysis engaging and fun
- **Comprehensive analysis** covering all aspects of TikTok usage

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Follow our coding standards** (ESLint configuration included)
4. **Test your changes thoroughly** on multiple devices
5. **Commit with descriptive messages** (`git commit -m 'Add amazing feature'`)
6. **Push to your branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request** with detailed description

### **Development Guidelines**
- **Mobile-first**: Always test on mobile devices first
- **Accessibility**: Ensure proper contrast ratios and keyboard navigation
- **Performance**: Optimize images, animations, and data processing
- **Code Quality**: Follow React best practices and use TypeScript when possible

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TikTok** for providing comprehensive data export capabilities
- **Google Gemini** for powerful AI analysis and insights
- **Auth0** for secure, customizable authentication
- **React & Vite Teams** for incredible developer experience
- **Open Source Community** for the amazing libraries and tools
- **Data Hackfest 2025** for inspiring innovation in data visualization

---

## 🎉 **Built with ❤️ for Data Hackfest 2025**

**EXPOSED** represents the future of personal data analysis - where beautiful design meets powerful insights, where TikTok aesthetics meet meaningful self-discovery, and where complex data becomes simple stories.

*Transform your digital footprint into beautiful insights with EXPOSED - your TikTok, reflected back at you.* ✨📊🌈

---

### 🔗 **Quick Links**
- **Live Demo**: [Coming Soon]
- **Documentation**: [In this README]
- **Issues**: [GitHub Issues]
- **Discussions**: [GitHub Discussions]

### 📞 **Support**
Having trouble? Check our comprehensive user guide or open an issue for help!

**Ready to discover your digital self? Let's get started!** 🚀 