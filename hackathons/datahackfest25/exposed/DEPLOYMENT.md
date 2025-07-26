# 🚀 EXPOSED Deployment Guide

> **Get your TikTok data analysis app live for the world to use!**

This guide will help you deploy **EXPOSED** to the internet so anyone can use your amazing app.

## 🌟 **Deployment Overview**

We'll deploy using the best free platforms:
- **Frontend**: Vercel (Lightning fast, free tier)
- **Backend**: Railway (Modern, developer-friendly)
- **Database**: MongoDB Atlas (Already set up)

## 🎯 **Step 1: Deploy Frontend to Vercel**

### **Option A: Quick Deploy with Vercel CLI (Recommended)**

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Login to Vercel**
```bash
vercel login
```

3. **Deploy from Frontend Directory**
```bash
cd frontend
vercel
```

4. **Follow the prompts:**
   - **Set up and deploy?** → Yes
   - **Which scope?** → Your personal account
   - **Link to existing project?** → No
   - **Project name?** → `exposed-app` (or your choice)
   - **Directory?** → `./` (current directory)
   - **Want to override settings?** → No

### **Option B: Deploy via GitHub (Alternative)**

1. **Push your code to GitHub**
2. **Go to [Vercel.com](https://vercel.com)**
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Set build settings:**
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### **Environment Variables for Frontend**

In Vercel dashboard, add these environment variables:
```bash
VITE_AUTH0_DOMAIN=your-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id
VITE_AUTH0_CALLBACK_URL=https://your-app.vercel.app
```

## ⚙️ **Step 2: Deploy Backend to Railway**

### **Quick Railway Deployment**

1. **Go to [Railway.app](https://railway.app)**
2. **Sign up/Login with GitHub**
3. **Click "New Project"**
4. **Choose "Deploy from GitHub repo"**
5. **Select your repository**
6. **Set root directory to `backend`**

### **Environment Variables for Backend**

In Railway dashboard, add these variables:
```bash
MONGODB_URI=your_mongodb_atlas_connection_string
GEMINI_API_KEY=your_gemini_api_key
PORT=4000
```

### **Alternative: Deploy Backend to Render**

1. **Go to [Render.com](https://render.com)**
2. **Sign up/Login**
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repository**
5. **Settings:**
   - **Name**: `exposed-backend`
   - **Root Directory**: `backend`
   - **Build Command**: `npm install`
   - **Start Command**: `node app.js`

## 🔧 **Step 3: Update CORS Settings**

Update your backend `app.js` to allow your frontend domain:

```javascript
// In backend/app.js
app.use(cors({
  origin: [
    'http://localhost:5173',
    'https://your-app.vercel.app', // Add your Vercel URL
    'https://your-custom-domain.com' // If you have a custom domain
  ]
}));
```

## 🔐 **Step 4: Update Auth0 Settings**

1. **Go to Auth0 Dashboard**
2. **Update Allowed Callback URLs:**
```
https://your-app.vercel.app,
http://localhost:5173
```

3. **Update Allowed Logout URLs:**
```
https://your-app.vercel.app,
http://localhost:5173
```

4. **Update Allowed Web Origins:**
```
https://your-app.vercel.app,
http://localhost:5173
```

## 🌐 **Step 5: Connect Frontend to Backend**

Update your frontend to use the production backend URL:

```javascript
// In frontend/src/pages/Dashboard.jsx
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://your-backend.railway.app' 
  : 'http://localhost:4000';

// Update fetch calls to use API_BASE_URL
const response = await fetch(`${API_BASE_URL}/analyze`, {
  // ... your existing code
});
```

## 🎨 **Step 6: Custom Domain (Optional)**

### **For Vercel:**
1. **Buy a domain** (Namecheap, GoDaddy, etc.)
2. **In Vercel Dashboard** → Domains
3. **Add your domain**
4. **Update DNS settings** as instructed

### **Example Custom Domains:**
- `exposed.app`
- `tiktokmirror.com`
- `yourdigitalself.app`
- `datatiktok.com`

## 🚀 **Step 7: Final Testing**

1. **Test the live app:**
   - Upload a TikTok JSON file
   - Verify all visualizations work
   - Test Auth0 login/logout
   - Check mobile responsiveness

2. **Performance Check:**
   - Use [PageSpeed Insights](https://pagespeed.web.dev/)
   - Aim for 90+ scores

3. **Share with the world!** 🎉

## 📊 **Quick Commands Reference**

### **Vercel Deployment**
```bash
# Install CLI
npm install -g vercel

# Deploy
cd frontend
vercel

# Check deployment
vercel --prod
```

### **Update Deployment**
```bash
# Frontend
cd frontend
vercel --prod

# Backend (push to GitHub, auto-deploys)
git add .
git commit -m "Update backend"
git push origin main
```

## 🔍 **Troubleshooting**

### **Common Issues & Solutions:**

1. **CORS Errors**
   - Update backend CORS settings with your frontend URL
   - Ensure both HTTP and HTTPS versions are included

2. **Auth0 Redirect Issues**
   - Check callback URLs in Auth0 dashboard
   - Verify environment variables are set correctly

3. **API Connection Errors**
   - Ensure backend is deployed and running
   - Check environment variables on both platforms
   - Verify API endpoints are correct

4. **Build Failures**
   - Check for missing dependencies
   - Verify build commands are correct
   - Review build logs for specific errors

## 🎯 **Pro Tips**

1. **Use Environment Variables** for all sensitive data
2. **Set up Auto-Deploy** from GitHub for easy updates
3. **Monitor Performance** with platform analytics
4. **Set up Custom Domains** for professional appearance
5. **Add HTTPS** (automatic with Vercel/Railway)

## 🌟 **After Deployment**

### **Share Your App:**
- **Social Media**: Share your live demo
- **Hackathon Submission**: Include live URL
- **Portfolio**: Add to your developer portfolio
- **Community**: Share on Reddit, Discord, etc.

### **Analytics & Monitoring:**
- **Vercel Analytics**: Track usage and performance
- **Railway Metrics**: Monitor backend performance
- **Error Tracking**: Set up Sentry for production errors

## 🎉 **Success Checklist**

- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway/Render
- [ ] Environment variables configured
- [ ] Auth0 updated with production URLs
- [ ] CORS configured correctly
- [ ] API endpoints updated
- [ ] Custom domain set up (optional)
- [ ] App tested end-to-end
- [ ] Performance optimized
- [ ] Shared with the world! 🌍

---

**Congratulations! Your EXPOSED app is now live and ready for Data Hackfest 2025!** 🏆✨

**Live URLs:**
- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-backend.railway.app`

**Ready to impress the judges and users worldwide!** 🚀📊🌈 