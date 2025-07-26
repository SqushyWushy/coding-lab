import { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { marked } from 'marked';
import ActivityHeatmap from '../components/ActivityHeatmap.jsx';
import ActivityClock from '../components/ActivityClock.jsx';
import EngagementTrends from '../components/EngagementTrends.jsx';
import WordCloud from '../components/WordCloud.jsx';
import WeeklyPattern from '../components/WeeklyPattern.jsx';
import DataGuide from '../components/DataGuide.jsx';

function Dashboard() {
  const { user, logout } = useAuth0();
  const [file, setFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState(null);
  const [isDragOver, setIsDragOver] = useState(false);
  const [loadingProgress, setLoadingProgress] = useState(0);
  const [loadingStage, setLoadingStage] = useState('');
  const [showDataGuide, setShowDataGuide] = useState(false);

  // Configure marked options for better rendering
  useEffect(() => {
    marked.setOptions({
      breaks: true,
      gfm: true,
    });
  }, []);

  // Loading stages with descriptions
  const loadingStages = [
    { progress: 15, text: 'Uploading your data...', emoji: '📤' },
    { progress: 30, text: 'Parsing TikTok data...', emoji: '🔍' },
    { progress: 50, text: 'Analyzing patterns...', emoji: '📊' },
    { progress: 70, text: 'Computing insights...', emoji: '🧠' },
    { progress: 85, text: 'Generating AI reflection...', emoji: '✨' },
    { progress: 100, text: 'Finalizing your report...', emoji: '🎉' }
  ];

  // Simulate progressive loading
  const simulateProgress = () => {
    let currentStage = 0;
    setLoadingProgress(0);
    setLoadingStage(loadingStages[0].text);

    const progressInterval = setInterval(() => {
      if (currentStage < loadingStages.length) {
        const stage = loadingStages[currentStage];
        setLoadingProgress(stage.progress);
        setLoadingStage(stage.text);
        currentStage++;
      } else {
        clearInterval(progressInterval);
      }
    }, 800); // Progress every 800ms

    return progressInterval;
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    processFile(selectedFile);
  };

  const processFile = (selectedFile) => {
    if (selectedFile && selectedFile.type === "application/json") {
      setFile(selectedFile);
      setError(null);
    } else {
      setError("Please select a valid JSON file");
      setFile(null);
    }
  };

  // Drag and drop handlers
  const handleDragEnter = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(false);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(false);
    
    const files = Array.from(e.dataTransfer.files);
    if (files.length > 0) {
      processFile(files[0]);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file first");
      return;
    }

    setIsLoading(true);
    setError(null);

    // Start the progress simulation
    const progressInterval = simulateProgress();

    try {
      const formData = new FormData();
      formData.append("tiktokData", file);

      // Use environment-based API URL
      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:4000';

      const response = await fetch(`${API_BASE_URL}/analyze`, {
        method: "POST",
        body: formData,
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Analysis failed");
      }

      // Ensure we reach 100% before showing results
      clearInterval(progressInterval);
      setLoadingProgress(100);
      setLoadingStage('Complete! 🎉');
      
      // Small delay to show completion
      setTimeout(() => {
        setAnalysis(result.data);
        setIsLoading(false);
      }, 500);

    } catch (err) {
      clearInterval(progressInterval);
      setError(err.message);
      setIsLoading(false);
      setLoadingProgress(0);
      setLoadingStage('');
    }
  };

  const handleLogout = () => {
    logout({ returnTo: window.location.origin });
  };

  const formatNumber = (num) => {
    if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
    if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
    return num.toLocaleString();
  };

  const formatTime = (hours) => {
    if (hours >= 24) {
      const days = Math.floor(hours / 24);
      const remainingHours = hours % 24;
      return `${days}d ${remainingHours.toFixed(1)}h`;
    }
    return `${hours.toFixed(1)}h`;
  };

  // Function to render markdown content
  const renderMarkdown = (content) => {
    if (!content) return '';
    return marked(content);
  };

  return (
    <div 
      style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #f9fafb 0%, #e0f2fe 100%)',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
      }}
    >
      {/* Header */}
      <header style={{ padding: '2rem' }}>
        <div style={{ maxWidth: '64rem', margin: '0 auto' }}>
          <div 
            style={{
              backgroundColor: 'white',
              padding: '1.5rem',
              borderRadius: '1rem',
              boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              <div 
                style={{
                  width: '2.5rem',
                  height: '2.5rem',
                  background: 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)',
                  borderRadius: '0.75rem',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}
              >
                <span style={{ color: 'white', fontSize: '1.25rem' }}>✨</span>
              </div>
              <div>
                <h1 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', margin: 0 }}>
                  EXPOSED
                </h1>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>
                  Your digital mirror
                </p>
              </div>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              <div style={{ textAlign: 'right' }}>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>
                  Welcome back,
                </p>
                <p style={{ fontWeight: '500', color: '#111827', margin: 0 }}>
                  {user?.name || user?.email || 'User'}
                </p>
              </div>
              <button
                onClick={handleLogout}
                style={{
                  padding: '0.5rem 1rem',
                  backgroundColor: '#ef4444',
                  color: 'white',
                  fontSize: '0.875rem',
                  fontWeight: '500',
                  borderRadius: '0.5rem',
                  border: 'none',
                  cursor: 'pointer',
                  transition: 'background-color 0.2s'
                }}
                onMouseOver={(e) => e.target.style.backgroundColor = '#dc2626'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#ef4444'}
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>

      <main style={{ maxWidth: '64rem', margin: '0 auto', padding: '0 2rem 2rem' }}>
        {/* Upload Section */}
        {!analysis && (
          <div style={{ padding: '4rem 0' }}>
            <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
              <h2 
                style={{
                  fontSize: 'clamp(2rem, 4vw, 3rem)',
                  fontWeight: '600',
                  marginBottom: '1rem',
                  letterSpacing: '-0.025em',
                  background: 'linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD)',
                  backgroundSize: '300% 300%',
                  WebkitBackgroundClip: 'text',
                  backgroundClip: 'text',
                  color: 'transparent',
                  animation: 'tiktokGradient 5s ease infinite'
                }}
              >
                Ready to See Your Reflection?
              </h2>
              <p 
                style={{
                  fontSize: '1.25rem',
                  color: '#6b7280',
                  fontWeight: '300',
                  maxWidth: '32rem',
                  margin: '0 auto 1.5rem',
                  lineHeight: '1.6'
                }}
              >
                Upload your TikTok data export and discover the patterns, habits, and personality traits hidden in your digital footprint.
              </p>
              
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <button
                  onClick={() => setShowDataGuide(true)}
                  style={{
                    padding: '0.75rem 1.5rem',
                    backgroundColor: '#3b82f6',
                    color: 'white',
                    border: 'none',
                    borderRadius: '0.5rem',
                    fontSize: '0.875rem',
                    fontWeight: '500',
                    cursor: 'pointer',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    transition: 'background-color 0.2s'
                  }}
                  onMouseOver={(e) => e.target.style.backgroundColor = '#2563eb'}
                  onMouseOut={(e) => e.target.style.backgroundColor = '#3b82f6'}
                >
                  <span>📥</span>
                  <span>How to Get Your TikTok Data</span>
                </button>
                <p style={{ fontSize: '0.75rem', color: '#9ca3af', marginTop: '0.5rem' }}>
                  Don't have your data yet? Click above for step-by-step instructions
                </p>
              </div>
            </div>
            
            <form onSubmit={handleSubmit} style={{ maxWidth: '32rem', margin: '0 auto' }}>
              <div 
                style={{
                  backgroundColor: 'white',
                  borderRadius: '1rem',
                  padding: '2rem',
                  boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                  marginBottom: '1.5rem'
                }}
              >
                <input
                  type="file"
                  accept=".json"
                  onChange={handleFileChange}
                  style={{ display: 'none' }}
                  id="file-upload"
                />
                <label
                  htmlFor="file-upload"
                  style={{
                    display: 'block',
                    cursor: 'pointer',
                    textAlign: 'center',
                    padding: '3rem 2rem',
                    border: `2px dashed ${isDragOver ? '#3b82f6' : (file ? '#10b981' : '#d1d5db')}`,
                    borderRadius: '0.75rem',
                    transition: 'all 0.2s',
                    backgroundColor: isDragOver ? '#eff6ff' : (file ? '#f0fdf4' : 'transparent'),
                    transform: isDragOver ? 'scale(1.02)' : 'scale(1)'
                  }}
                  onMouseOver={(e) => {
                    if (!isDragOver) {
                      e.target.style.borderColor = '#3b82f6';
                      e.target.style.backgroundColor = '#f0f9ff';
                    }
                  }}
                  onMouseOut={(e) => {
                    if (!isDragOver) {
                      e.target.style.borderColor = file ? '#10b981' : '#d1d5db';
                      e.target.style.backgroundColor = file ? '#f0fdf4' : 'transparent';
                    }
                  }}
                  onDragEnter={handleDragEnter}
                  onDragLeave={handleDragLeave}
                  onDragOver={handleDragOver}
                  onDrop={handleDrop}
                >
                  <div 
                    style={{
                      width: '3rem',
                      height: '3rem',
                      backgroundColor: isDragOver ? '#dbeafe' : (file ? '#dcfce7' : '#f3f4f6'),
                      borderRadius: '0.75rem',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      margin: '0 auto 1rem',
                      transition: 'all 0.2s'
                    }}
                  >
                    <span style={{ fontSize: '1.5rem' }}>
                      {isDragOver ? '⬇️' : (file ? '✅' : '📄')}
                    </span>
                  </div>
                  <p style={{ fontSize: '1.125rem', fontWeight: '500', color: '#111827', margin: '0 0 0.5rem' }}>
                    {isDragOver 
                      ? "Drop your file here!" 
                      : file 
                        ? file.name 
                        : "Drag & drop or click to choose file"}
                  </p>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>
                    {isDragOver 
                      ? "Release to upload your TikTok data" 
                      : file 
                        ? "File selected ✓ Ready to analyze!" 
                        : "TikTok JSON file from Settings → Privacy → Download data"}
                  </p>
                  {!file && !isDragOver && (
                    <button
                      onClick={() => setShowDataGuide(true)}
                      style={{
                        marginTop: '1rem',
                        padding: '0.5rem 1rem',
                        backgroundColor: 'transparent',
                        color: '#3b82f6',
                        border: '1px solid #3b82f6',
                        borderRadius: '0.375rem',
                        fontSize: '0.75rem',
                        fontWeight: '500',
                        cursor: 'pointer',
                        transition: 'all 0.2s'
                      }}
                      onMouseOver={(e) => {
                        e.target.style.backgroundColor = '#3b82f6';
                        e.target.style.color = 'white';
                      }}
                      onMouseOut={(e) => {
                        e.target.style.backgroundColor = 'transparent';
                        e.target.style.color = '#3b82f6';
                      }}
                    >
                      Need help getting your data?
                    </button>
                  )}
                </label>
              </div>

              {error && (
                <div 
                  style={{
                    backgroundColor: '#fef2f2',
                    border: '1px solid #fecaca',
                    color: '#dc2626',
                    padding: '1rem',
                    borderRadius: '0.5rem',
                    marginBottom: '1.5rem',
                    fontSize: '0.875rem'
                  }}
                >
                  {error}
                </div>
              )}

{isLoading ? (
                <div 
                  style={{
                    width: '100%',
                    padding: '1.5rem',
                    backgroundColor: 'white',
                    borderRadius: '0.75rem',
                    border: '1px solid #e5e7eb'
                  }}
                >
                  {/* Progress Header */}
                  <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
                    <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>
                      {loadingStages.find(stage => stage.text === loadingStage)?.emoji || '⚡'}
                    </div>
                    <h3 style={{ 
                      fontSize: '1.125rem', 
                      fontWeight: '600', 
                      marginBottom: '0.25rem',
                      background: 'linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7)',
                      backgroundSize: '200% 200%',
                      WebkitBackgroundClip: 'text',
                      backgroundClip: 'text',
                      color: 'transparent',
                      animation: 'tiktokGradient 3s ease infinite'
                    }}>
                      Analyzing Your Digital Mirror
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                      {loadingStage}
                    </p>
                  </div>

                  {/* Progress Bar Container */}
                  <div 
                    style={{
                      width: '100%',
                      height: '8px',
                      backgroundColor: '#f3f4f6',
                      borderRadius: '4px',
                      overflow: 'hidden',
                      marginBottom: '0.75rem'
                    }}
                  >
                    {/* Progress Bar Fill */}
                    <div 
                      style={{
                        width: `${loadingProgress}%`,
                        height: '100%',
                        background: 'linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 25%, #45B7D1 50%, #96CEB4 75%, #FFEAA7 100%)',
                        borderRadius: '4px',
                        transition: 'width 0.5s ease-in-out',
                        boxShadow: '0 0 10px rgba(59, 130, 246, 0.3)'
                      }}
                    />
                  </div>

                  {/* Progress Percentage */}
                  <div style={{ textAlign: 'center' }}>
                    <span style={{ fontSize: '0.875rem', fontWeight: '500', color: '#3b82f6' }}>
                      {loadingProgress}%
                    </span>
                  </div>
                </div>
              ) : (
                <button
                  type="submit"
                  disabled={!file}
                  style={{
                    width: '100%',
                    padding: '1rem 2rem',
                    background: file 
                      ? 'linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 25%, #45B7D1 50%, #96CEB4 100%)' 
                      : '#9ca3af',
                    color: 'white',
                    fontSize: '1rem',
                    fontWeight: '600',
                    borderRadius: '0.75rem',
                    border: 'none',
                    cursor: file ? 'pointer' : 'not-allowed',
                    transition: 'all 0.3s ease',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '0.75rem',
                    boxShadow: file ? '0 4px 15px rgba(255, 107, 107, 0.3)' : 'none',
                    transform: 'translateY(0)',
                    backgroundSize: '200% 200%',
                    animation: file ? 'tiktokGradient 4s ease infinite' : 'none'
                  }}
                  onMouseOver={(e) => {
                    if (file) {
                      e.target.style.transform = 'translateY(-2px)';
                      e.target.style.boxShadow = '0 8px 25px rgba(255, 107, 107, 0.4)';
                    }
                  }}
                  onMouseOut={(e) => {
                    if (file) {
                      e.target.style.transform = 'translateY(0)';
                      e.target.style.boxShadow = '0 4px 15px rgba(255, 107, 107, 0.3)';
                    }
                  }}
                >
                  <span>✨</span>
                  <span>Reveal My Digital Mirror</span>
                </button>
              )}
            </form>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div style={{ padding: '2rem 0', marginBottom: '3rem' }}>
            {/* Welcome Banner */}
            <div 
              style={{
                textAlign: 'center',
                marginBottom: '3rem',
                backgroundColor: 'white',
                padding: '3rem 2rem',
                borderRadius: '1rem',
                boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
              }}
            >
              <div 
                style={{
                  width: '4rem',
                  height: '4rem',
                  background: 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)',
                  borderRadius: '1rem',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  margin: '0 auto 1.5rem'
                }}
              >
                <span style={{ color: 'white', fontSize: '2rem' }}>✨</span>
              </div>
              <h1 
                style={{
                  fontSize: 'clamp(2rem, 4vw, 3rem)',
                  fontWeight: '600',
                  marginBottom: '1rem',
                  letterSpacing: '-0.025em',
                  background: 'linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD)',
                  backgroundSize: '300% 300%',
                  WebkitBackgroundClip: 'text',
                  backgroundClip: 'text',
                  color: 'transparent',
                  animation: 'tiktokGradient 6s ease infinite'
                }}
              >
                Your Digital Mirror
              </h1>
              <p 
                style={{
                  fontSize: '1.25rem',
                  color: '#6b7280',
                  fontWeight: '300',
                  maxWidth: '32rem',
                  margin: '0 auto',
                  lineHeight: '1.6'
                }}
              >
                Here's what your TikTok data reveals about your digital behavior and personality
              </p>
            </div>

            {/* Top-Level Metrics */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  Your Digital Footprint
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  The big numbers that tell your story
                </p>
              </div>
              
              <div 
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                  gap: '1.5rem'
                }}
              >
                {[
                  {
                    icon: "▶️",
                    label: "Videos Watched",
                    value: formatNumber(analysis.summary.totalVideosWatched),
                    color: "#3b82f6"
                  },
                  {
                    icon: "⏰",
                    label: "Time Spent",
                    value: formatTime(analysis.summary.totalWatchTime.hours),
                    color: "#10b981"
                  },
                  {
                    icon: "📍",
                    label: "Miles Scrolled",
                    value: analysis.summary.scrollDistance.miles.toFixed(2),
                    color: "#8b5cf6"
                  },
                  {
                    icon: "❤️",
                    label: "Likes Given",
                    value: formatNumber(analysis.summary.totalLikes),
                    color: "#ec4899"
                  }
                ].map((stat, index) => (
                  <div 
                    key={index}
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                      textAlign: 'center'
                    }}
                  >
                    <div 
                      style={{
                        width: '3rem',
                        height: '3rem',
                        backgroundColor: `${stat.color}15`,
                        border: `1px solid ${stat.color}30`,
                        borderRadius: '0.75rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        margin: '0 auto 1rem',
                        fontSize: '1.5rem'
                      }}
                    >
                      {stat.icon}
                    </div>
                    <div style={{ fontSize: '2rem', fontWeight: '300', color: '#111827', marginBottom: '0.5rem' }}>
                      {stat.value}
                    </div>
                    <div style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                      {stat.label}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Streak + Peak Day Summary */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  Your Digital Patterns
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  When and how you engage with content
                </p>
              </div>
              
              <div 
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
                  gap: '1.5rem'
                }}
              >
                <div 
                  style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '1rem',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
                    <div 
                      style={{
                        width: '3rem',
                        height: '3rem',
                        backgroundColor: '#f59e0b15',
                        border: '1px solid #f59e0b30',
                        borderRadius: '0.75rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '1.5rem'
                      }}
                    >
                      🔥
                    </div>
                    <div>
                      <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', margin: 0 }}>
                        Your Longest Streak
                      </h3>
                      <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>
                        Consecutive days of activity
                      </p>
                    </div>
                  </div>
                  <div style={{ fontSize: '2.5rem', fontWeight: '300', color: '#f59e0b', marginBottom: '0.5rem' }}>
                    {analysis.summary.longestStreak.days} days
                  </div>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    From {analysis.summary.longestStreak.startDate} to {analysis.summary.longestStreak.endDate}
                  </p>
                </div>

                <div 
                  style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '1rem',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
                    <div 
                      style={{
                        width: '3rem',
                        height: '3rem',
                        backgroundColor: '#10b98115',
                        border: '1px solid #10b98130',
                        borderRadius: '0.75rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '1.5rem'
                      }}
                    >
                      📈
                    </div>
                    <div>
                      <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', margin: 0 }}>
                        Peak Activity Day
                      </h3>
                      <p style={{ fontSize: '0.875rem', color: '#6b7280', margin: 0 }}>
                        Your most engaged day
                      </p>
                    </div>
                  </div>
                  <div style={{ fontSize: '2.5rem', fontWeight: '300', color: '#10b981', marginBottom: '0.5rem' }}>
                    {analysis.summary.mostActiveDay.videos} videos
                  </div>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    On {new Date(analysis.summary.mostActiveDay.date).toLocaleDateString()}
                  </p>
                </div>
              </div>
            </div>

            {/* Comment/Search Behavior */}
            {analysis.summary.comments.totalComments > 0 && (
              <div style={{ marginBottom: '3rem' }}>
                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                  <h2 
                    style={{
                      fontSize: '1.875rem',
                      fontWeight: '300',
                      color: '#111827',
                      marginBottom: '0.5rem',
                      letterSpacing: '-0.025em'
                    }}
                  >
                    Your Social Voice
                  </h2>
                  <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                    How you interact and express yourself
                  </p>
                </div>
                
                <div 
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                    gap: '1.5rem',
                    marginBottom: '2rem'
                  }}
                >
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '1.5rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                      textAlign: 'center'
                    }}
                  >
                    <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>💬</div>
                    <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#111827', marginBottom: '0.25rem' }}>
                      {analysis.summary.comments.totalComments}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Total Comments</div>
                  </div>
                  
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '1.5rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                      textAlign: 'center'
                    }}
                  >
                    <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>📝</div>
                    <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#111827', marginBottom: '0.25rem' }}>
                      {analysis.summary.comments.averageCommentLength}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Avg. Comment Length</div>
                  </div>
                  
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '1.5rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                      textAlign: 'center'
                    }}
                  >
                    <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>😊</div>
                    <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#111827', marginBottom: '0.25rem' }}>
                      {analysis.summary.comments.emojiUsage}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Emoji Usage</div>
                  </div>
                </div>

                {/* Two-column layout for comments and hashtags */}
                <div 
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
                    gap: '2rem',
                    marginBottom: '2rem'
                  }}
                >
                  {/* Top Words */}
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                    }}
                  >
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '1rem' }}>
                      Your Most Used Words
                    </h3>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.75rem' }}>
                      {Object.entries(analysis.summary.comments.topCommentWords)
                        .slice(0, 12)
                        .map(([word, count], index) => (
                          <span
                            key={index}
                            style={{
                              padding: '0.5rem 1rem',
                              backgroundColor: '#f3f4f6',
                              color: '#374151',
                              borderRadius: '9999px',
                              fontSize: '0.875rem'
                            }}
                          >
                            {word} ({count})
                          </span>
                        ))}
                    </div>
                  </div>

                  {/* Top Hashtags */}
                  {analysis.summary.hashtags && analysis.summary.hashtags.length > 0 && (
                    <div 
                      style={{
                        backgroundColor: 'white',
                        padding: '2rem',
                        borderRadius: '1rem',
                        boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                      }}
                    >
                      <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '1rem' }}>
                        🏷️ Top Hashtags
                      </h3>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                        {analysis.summary.hashtags
                          .slice(0, 10)
                          .map((hashtag, index) => (
                            <div
                              key={index}
                              style={{
                                display: 'flex',
                                justifyContent: 'space-between',
                                alignItems: 'center',
                                padding: '0.75rem',
                                backgroundColor: '#f8fafc',
                                borderRadius: '0.5rem'
                              }}
                            >
                              <span style={{ fontSize: '0.875rem', color: '#1f2937', fontWeight: '500' }}>
                                #{hashtag.tag}
                              </span>
                              <span style={{ fontSize: '0.75rem', color: '#6b7280', fontWeight: '600' }}>
                                {hashtag.count}
                              </span>
                            </div>
                          ))}
                      </div>
                    </div>
                  )}
                </div>

                {/* Longest Comments */}
                {analysis.summary.comments.longestComments && analysis.summary.comments.longestComments.length > 0 && (
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                      marginBottom: '2rem'
                    }}
                  >
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '1rem' }}>
                      📄 Your Longest Comments
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                      When you had the most to say
                    </p>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                      {analysis.summary.comments.longestComments
                        .slice(0, 10)
                        .map((comment, index) => (
                          <div
                            key={index}
                            style={{
                              padding: '1rem',
                              backgroundColor: '#f8fafc',
                              borderRadius: '0.75rem',
                              borderLeft: '4px solid #3b82f6'
                            }}
                          >
                            <div style={{ fontSize: '0.875rem', color: '#374151', lineHeight: '1.5', marginBottom: '0.5rem' }}>
                              "{comment.text}"
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'between', alignItems: 'center', fontSize: '0.75rem', color: '#6b7280' }}>
                              <span>{comment.length} characters</span>
                              {comment.date && (
                                <span style={{ marginLeft: 'auto' }}>
                                  {new Date(comment.date).toLocaleDateString()}
                                </span>
                              )}
                            </div>
                          </div>
                        ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* TikTok Usage Over Time Chart */}
            {analysis.summary.activityOverTime && (
              <div style={{ marginBottom: '3rem' }}>
                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                  <h2 
                    style={{
                      fontSize: '1.875rem',
                      fontWeight: '300',
                      color: '#111827',
                      marginBottom: '0.5rem',
                      letterSpacing: '-0.025em'
                    }}
                  >
                    📈 Activity Over Time
                  </h2>
                  <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                    Your TikTok usage patterns throughout the months
                  </p>
                </div>
                
                <div 
                  style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '1rem',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                    marginBottom: '2rem'
                  }}
                >
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                    {Object.entries(analysis.summary.activityOverTime)
                      .sort((a, b) => new Date(a[0]) - new Date(b[0]))
                      .map(([month, activity], index) => {
                        const maxActivity = Math.max(...Object.values(analysis.summary.activityOverTime).map(a => a.videos || 0));
                        const percentage = maxActivity > 0 ? ((activity.videos || 0) / maxActivity) * 100 : 0;
                        
                        return (
                          <div key={index} style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                            <div style={{ minWidth: '120px', fontSize: '0.875rem', color: '#6b7280', fontWeight: '500' }}>
                              {new Date(month + '-01').toLocaleDateString('en-US', { year: 'numeric', month: 'short' })}
                            </div>
                            
                            <div style={{ flex: 1, display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                              <div 
                                style={{
                                  flex: 1,
                                  height: '24px',
                                  backgroundColor: '#f3f4f6',
                                  borderRadius: '12px',
                                  overflow: 'hidden',
                                  position: 'relative'
                                }}
                              >
                                <div 
                                  style={{
                                    width: `${percentage}%`,
                                    height: '100%',
                                    background: 'linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%)',
                                    borderRadius: '12px',
                                    transition: 'width 0.5s ease-in-out'
                                  }}
                                />
                              </div>
                              
                              <div style={{ minWidth: '60px', textAlign: 'right' }}>
                                <span style={{ fontSize: '0.875rem', fontWeight: '600', color: '#111827' }}>
                                  {formatNumber(activity.videos || 0)}
                                </span>
                                <span style={{ fontSize: '0.75rem', color: '#6b7280', marginLeft: '0.25rem' }}>
                                  videos
                                </span>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                  </div>
                </div>
              </div>
            )}

            {/* Timeline Breakdown */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  Your Digital Timeline
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  How your TikTok journey evolved over time
                </p>
              </div>
              
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                {Object.entries(analysis.summary.yearlyAnalysis)
                  .sort((a, b) => b[0] - a[0])
                  .map(([year, data], index) => (
                    <div
                      key={year}
                      style={{
                        backgroundColor: 'white',
                        padding: '1.5rem',
                        borderRadius: '1rem',
                        boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                        border: year === analysis.summary.mostActiveYear.year ? '2px solid #8b5cf6' : '1px solid #e5e7eb'
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
                        <h3 style={{ fontSize: '1.5rem', fontWeight: '600', color: '#111827', margin: 0 }}>
                          {year}
                        </h3>
                        {year === analysis.summary.mostActiveYear.year && (
                          <span 
                            style={{
                              padding: '0.25rem 0.75rem',
                              backgroundColor: '#8b5cf6',
                              color: 'white',
                              borderRadius: '9999px',
                              fontSize: '0.75rem',
                              fontWeight: '500'
                            }}
                          >
                            Most Active Year
                          </span>
                        )}
                      </div>
                      <div 
                        style={{
                          display: 'grid',
                          gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
                          gap: '1rem'
                        }}
                      >
                        <div style={{ textAlign: 'center' }}>
                          <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#3b82f6' }}>
                            {formatNumber(data.videos)}
                          </div>
                          <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Videos</div>
                        </div>
                        <div style={{ textAlign: 'center' }}>
                          <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#10b981' }}>
                            {data.searches}
                          </div>
                          <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Searches</div>
                        </div>
                        <div style={{ textAlign: 'center' }}>
                          <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#8b5cf6' }}>
                            {data.comments}
                          </div>
                          <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Comments</div>
                        </div>
                        <div style={{ textAlign: 'center' }}>
                          <div style={{ fontSize: '1.5rem', fontWeight: '300', color: '#f59e0b' }}>
                            {formatNumber(data.logins)}
                          </div>
                          <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>Logins</div>
                        </div>
                      </div>
                    </div>
                  ))}
              </div>
            </div>

            {/* Data Visualizations */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  📊 Visual Analytics
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  Interactive charts revealing your digital patterns
                </p>
              </div>

              {/* Activity Heatmap */}
              {analysis.summary.dailyActivity && (
                <div 
                  style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '1rem',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                    marginBottom: '2rem'
                  }}
                >
                  <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                    📅 Activity Heatmap
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                    GitHub-style contribution calendar showing your daily TikTok activity
                  </p>
                  <ActivityHeatmap dailyActivity={analysis.summary.dailyActivity} />
                </div>
              )}

              {/* Two-column layout for clock and weekly pattern */}
              <div 
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
                  gap: '2rem',
                  marginBottom: '2rem'
                }}
              >
                {/* 24-Hour Activity Clock */}
                {analysis.summary.hourlyActivity && (
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                    }}
                  >
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                      🕐 24-Hour Activity Clock
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                      Radial chart showing your peak activity hours
                    </p>
                    <ActivityClock hourlyActivity={analysis.summary.hourlyActivity} />
                  </div>
                )}

                {/* Weekly Pattern */}
                {analysis.summary.weeklyActivity && (
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                    }}
                  >
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                      📊 Weekly Activity Pattern
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                      Weekday vs weekend usage comparison
                    </p>
                    <WeeklyPattern weeklyActivity={analysis.summary.weeklyActivity} />
                  </div>
                )}
              </div>

              {/* Engagement Trends */}
              {analysis.summary.engagementTrends && (
                <div 
                  style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '1rem',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                    marginBottom: '2rem'
                  }}
                >
                  <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                    📈 Engagement Trends Over Time
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                    Multi-line chart tracking your videos, likes, comments, and searches
                  </p>
                  <EngagementTrends engagementTrends={analysis.summary.engagementTrends} />
                </div>
              )}

              {/* Word Clouds */}
              {analysis.summary.comments.topCommentWords && Object.keys(analysis.summary.comments.topCommentWords).length > 0 && (
                <div 
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
                    gap: '2rem',
                    marginBottom: '2rem'
                  }}
                >
                  <div 
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                    }}
                  >
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                      💬 Comment Word Cloud
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                      Most frequently used words in your comments
                    </p>
                    <WordCloud 
                      words={analysis.summary.comments.topCommentWords} 
                      title="Comment Words"
                    />
                  </div>

                  {/* Search word cloud if available */}
                  {analysis.summary.topSearches && analysis.summary.topSearches.length > 0 && (
                    <div 
                      style={{
                        backgroundColor: 'white',
                        padding: '2rem',
                        borderRadius: '1rem',
                        boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                      }}
                    >
                      <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                        🔍 Search Terms Cloud
                      </h3>
                      <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '1.5rem' }}>
                        Your most common search queries
                      </p>
                      <WordCloud 
                        words={analysis.summary.topSearches.reduce((acc, [term, count]) => {
                          acc[term] = count;
                          return acc;
                        }, {})} 
                        title="Search Terms"
                      />
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* AI Reflection */}
            <div 
              style={{
                backgroundColor: 'white',
                padding: '3rem',
                borderRadius: '1rem',
                boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
                marginBottom: '3rem'
              }}
            >
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  AI Reflection
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  A personalized analysis of your digital behavior
                </p>
              </div>
              
              <div 
                style={{
                  padding: '2rem',
                  backgroundColor: '#f8fafc',
                  borderRadius: '0.75rem',
                  border: '1px solid #e2e8f0'
                }}
              >
                <div 
                  className="markdown-content"
                  style={{
                    fontSize: '1rem',
                    color: '#374151',
                    lineHeight: '1.7'
                  }}
                  dangerouslySetInnerHTML={{ 
                    __html: renderMarkdown(analysis.aiSummary) 
                  }}
                />
              </div>
            </div>

            {/* Digital Wellness Tips */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <h2 
                  style={{
                    fontSize: '1.875rem',
                    fontWeight: '300',
                    color: '#111827',
                    marginBottom: '0.5rem',
                    letterSpacing: '-0.025em'
                  }}
                >
                  Digital Wellness
                </h2>
                <p style={{ color: '#6b7280', fontSize: '1rem', margin: 0 }}>
                  Tips for a healthier relationship with social media
                </p>
              </div>
              
              <div 
                style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                  gap: '1.5rem'
                }}
              >
                {[
                  {
                    icon: "☕",
                    title: "Take Breaks",
                    description: "Consider setting daily limits on your social media usage",
                    color: "#10b981"
                  },
                  {
                    icon: "🧠",
                    title: "Be Mindful",
                    description: "Notice how you feel before and after using social media",
                    color: "#3b82f6"
                  },
                  {
                    icon: "🛡️",
                    title: "Protect Privacy",
                    description: "Regularly review your privacy settings and data sharing",
                    color: "#8b5cf6"
                  }
                ].map((tip, index) => (
                  <div 
                    key={index}
                    style={{
                      backgroundColor: 'white',
                      padding: '2rem',
                      borderRadius: '1rem',
                      boxShadow: '0 4px 20px rgba(0,0,0,0.08)'
                    }}
                  >
                    <div 
                      style={{
                        width: '3rem',
                        height: '3rem',
                        backgroundColor: `${tip.color}15`,
                        border: `1px solid ${tip.color}30`,
                        borderRadius: '0.75rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        margin: '0 0 1rem 0',
                        fontSize: '1.5rem'
                      }}
                    >
                      {tip.icon}
                    </div>
                    <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#111827', marginBottom: '0.5rem' }}>
                      {tip.title}
                    </h3>
                    <p style={{ fontSize: '0.875rem', color: '#6b7280', lineHeight: '1.5' }}>
                      {tip.description}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* Reset Button */}
            <div style={{ textAlign: 'center' }}>
              <button
                onClick={() => {
                  setAnalysis(null);
                  setFile(null);
                  setError(null);
                }}
                style={{
                  padding: '1rem 2rem',
                  backgroundColor: '#6b7280',
                  color: 'white',
                  fontSize: '1rem',
                  fontWeight: '500',
                  borderRadius: '0.75rem',
                  border: 'none',
                  cursor: 'pointer',
                  transition: 'background-color 0.2s'
                }}
                onMouseOver={(e) => e.target.style.backgroundColor = '#4b5563'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#6b7280'}
              >
                Analyze Another File
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer style={{ padding: '2rem', textAlign: 'center' }}>
        <p 
          style={{
            fontSize: '0.875rem',
            fontWeight: '300',
            color: '#6b7280',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.5rem'
          }}
        >
          <span>🔒</span>
          <span>Built with ❤️ for Data Hackfest 2025 • Privacy First • AI Powered</span>
        </p>
      </footer>

      {/* Data Guide Modal */}
      {showDataGuide && (
        <DataGuide onClose={() => setShowDataGuide(false)} />
      )}
    </div>
  );
}

export default Dashboard; 