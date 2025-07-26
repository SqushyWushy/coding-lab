import { useState } from 'react';

const DataGuide = ({ onClose }) => {
  const [activeTab, setActiveTab] = useState('beginner');

  const steps = {
    beginner: [
      {
        step: 1,
        title: "Open TikTok App",
        description: "Launch the TikTok app on your phone (iOS or Android)",
        details: [
          "Make sure you're logged into your TikTok account",
          "If you don't have the app, download it from App Store or Google Play",
          "This process works the same on both iPhone and Android"
        ],
        icon: "📱",
        time: "30 seconds"
      },
      {
        step: 2,
        title: "Go to Your Profile",
        description: "Tap the 'Profile' tab at the bottom right of your screen",
        details: [
          "Look for the person icon at the bottom of the app",
          "This will take you to your personal profile page",
          "You should see your profile picture and follower count"
        ],
        icon: "👤",
        time: "10 seconds"
      },
      {
        step: 3,
        title: "Open Settings Menu",
        description: "Tap the three horizontal lines (☰) in the top right corner",
        details: [
          "Also called the 'hamburger menu'",
          "This opens the main settings and options",
          "If you can't find it, look for three dots (...) instead"
        ],
        icon: "⚙️",
        time: "10 seconds"
      },
      {
        step: 4,
        title: "Find Settings and Privacy",
        description: "Scroll down and tap 'Settings and privacy'",
        details: [
          "It's usually near the bottom of the menu",
          "The exact wording might vary slightly",
          "Look for anything mentioning 'Settings' or 'Privacy'"
        ],
        icon: "🔒",
        time: "20 seconds"
      },
      {
        step: 5,
        title: "Access Privacy Settings",
        description: "Tap on 'Privacy' in the settings menu",
        details: [
          "This section controls who can see your data",
          "Don't worry - downloading your data doesn't change any privacy settings",
          "Your data remains private to you"
        ],
        icon: "🛡️",
        time: "10 seconds"
      },
      {
        step: 6,
        title: "Request Your Data",
        description: "Look for 'Download your data' or 'Request data download'",
        details: [
          "This might be under a section called 'Personalization and data'",
          "TikTok is legally required to provide this (GDPR/CCPA)",
          "It's completely free and safe to request"
        ],
        icon: "📥",
        time: "30 seconds"
      },
      {
        step: 7,
        title: "Choose Data Format",
        description: "Select 'JSON' format when prompted (NOT TXT)",
        details: [
          "JSON is a computer-readable format our app can understand",
          "TXT format won't work with our analysis tool",
          "JSON contains much more detailed information"
        ],
        icon: "📄",
        time: "10 seconds"
      },
      {
        step: 8,
        title: "Submit Your Request",
        description: "Tap 'Request data download' to submit your request",
        details: [
          "TikTok will process your request",
          "You'll get a confirmation message",
          "The processing usually takes a few days"
        ],
        icon: "✅",
        time: "10 seconds"
      },
      {
        step: 9,
        title: "Wait for Email",
        description: "Check your email in 2-7 days for a download link",
        details: [
          "TikTok will email you when your data is ready",
          "Check your spam/junk folder if you don't see it",
          "The email will come from TikTok official address",
          "Don't worry if it takes up to a week - this is normal"
        ],
        icon: "📧",
        time: "2-7 days"
      },
      {
        step: 10,
        title: "Download Your Data",
        description: "Click the download link in the email to get your file",
        details: [
          "The file will be called something like 'user_data.json'",
          "It might be in a ZIP file that you need to extract",
          "Save it somewhere you can easily find it (like Downloads folder)",
          "The file contains all your TikTok activity data"
        ],
        icon: "💾",
        time: "2 minutes"
      }
    ],
    technical: [
      {
        step: 1,
        title: "Navigate to TikTok Privacy Settings",
        description: "Access via: Profile → Settings → Privacy → Download your data",
        details: [
          "Direct path: TikTok App → Profile Tab → ☰ Menu → Settings and privacy → Privacy",
          "Alternative: TikTok Web → Settings → Privacy and Safety → Download your data",
          "API endpoints are not publicly available for data export"
        ],
        icon: "🔧",
        time: "1 minute"
      },
      {
        step: 2,
        title: "Configure Data Export Parameters",
        description: "Select JSON format and specify data range if available",
        details: [
          "Format: JSON (required for our parser)",
          "Date range: All available data recommended",
          "Data types: All categories selected by default",
          "File structure will be nested JSON with activity categories"
        ],
        icon: "⚙️",
        time: "30 seconds"
      },
      {
        step: 3,
        title: "Submit GDPR/CCPA Data Request",
        description: "Initiate formal data portability request",
        details: [
          "Request type: Data portability under GDPR Article 20",
          "Processing time: 48 hours to 30 days (typically 3-7 days)",
          "Legal basis: User data subject rights",
          "No rate limiting on legitimate requests"
        ],
        icon: "📋",
        time: "Instant"
      },
      {
        step: 4,
        title: "Await Processing & Email Delivery",
        description: "Monitor for automated email with secure download link",
        details: [
          "Email source: noreply@tiktok.com or similar official domain",
          "Link format: Temporary authenticated download URL",
          "Expiration: Links typically expire in 7-14 days",
          "Security: Links are user-specific and time-limited"
        ],
        icon: "⏱️",
        time: "2-7 days"
      },
      {
        step: 5,
        title: "Download & Extract Data Archive",
        description: "Retrieve compressed data package and extract contents",
        details: [
          "File format: ZIP archive containing JSON files",
          "Main file: user_data.json (~5-50MB depending on activity)",
          "Structure: Nested objects with categories like Activity, Profile, etc.",
          "Encoding: UTF-8 with escaped Unicode characters"
        ],
        icon: "📦",
        time: "2 minutes"
      },
      {
        step: 6,
        title: "Validate Data Integrity",
        description: "Verify JSON structure and required fields",
        details: [
          "JSON validation: Use `jq` or online JSON validator",
          "Required fields: Activity.VideoList, Activity.LoginHistory",
          "File size: Should be >1KB (empty files indicate issues)",
          "Encoding check: Ensure proper UTF-8 without BOM"
        ],
        icon: "✅",
        time: "1 minute"
      }
    ]
  };

  const troubleshooting = [
    {
      problem: "Can't find 'Download your data' option",
      solutions: [
        "Update your TikTok app to the latest version",
        "Try accessing via TikTok website instead of mobile app",
        "Check if the feature is available in your region",
        "Look under 'Privacy and Safety' or 'Account' sections"
      ]
    },
    {
      problem: "Email never arrived",
      solutions: [
        "Check spam/junk folder thoroughly",
        "Wait up to 7 days - processing can be slow",
        "Try requesting again if it's been over a week",
        "Ensure your email address is correct in TikTok settings"
      ]
    },
    {
      problem: "Downloaded file is empty or corrupted",
      solutions: [
        "Re-download the file from the email link",
        "Try downloading on a different device or browser",
        "Check if you need to extract a ZIP file first",
        "Request your data again if file is still corrupted"
      ]
    },
    {
      problem: "File is not in JSON format",
      solutions: [
        "Make sure you selected JSON (not TXT) when requesting",
        "If you have a TXT file, you'll need to request again",
        "Look for a file ending in .json inside any ZIP archives",
        "Contact TikTok support if only TXT option is available"
      ]
    }
  ];

  return (
    <div 
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 1000,
        padding: '1rem'
      }}
      onClick={onClose}
    >
      <div 
        style={{
          backgroundColor: 'white',
          borderRadius: '1rem',
          maxWidth: '50rem',
          maxHeight: '90vh',
          overflow: 'hidden',
          boxShadow: '0 25px 50px rgba(0, 0, 0, 0.25)'
        }}
        onClick={e => e.stopPropagation()}
      >
        {/* Header */}
        <div 
          style={{
            padding: '2rem',
            borderBottom: '1px solid #e5e7eb',
            background: 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)',
            color: 'white'
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <h2 style={{ fontSize: '1.5rem', fontWeight: '600', margin: 0 }}>
                📥 How to Get Your TikTok Data
              </h2>
              <p style={{ margin: '0.5rem 0 0', opacity: 0.9 }}>
                Step-by-step guide to download your personal TikTok data
              </p>
            </div>
            <button
              onClick={onClose}
              style={{
                background: 'rgba(255, 255, 255, 0.2)',
                border: 'none',
                borderRadius: '0.5rem',
                color: 'white',
                fontSize: '1.5rem',
                width: '2.5rem',
                height: '2.5rem',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
            >
              ×
            </button>
          </div>
        </div>

        {/* Tab Navigation */}
        <div style={{ display: 'flex', borderBottom: '1px solid #e5e7eb' }}>
          <button
            onClick={() => setActiveTab('beginner')}
            style={{
              flex: 1,
              padding: '1rem',
              border: 'none',
              backgroundColor: activeTab === 'beginner' ? '#f0f9ff' : 'white',
              color: activeTab === 'beginner' ? '#3b82f6' : '#6b7280',
              fontWeight: activeTab === 'beginner' ? '600' : '400',
              cursor: 'pointer',
              borderBottom: activeTab === 'beginner' ? '2px solid #3b82f6' : 'none'
            }}
          >
            🌟 Beginner Guide
          </button>
          <button
            onClick={() => setActiveTab('technical')}
            style={{
              flex: 1,
              padding: '1rem',
              border: 'none',
              backgroundColor: activeTab === 'technical' ? '#f0f9ff' : 'white',
              color: activeTab === 'technical' ? '#3b82f6' : '#6b7280',
              fontWeight: activeTab === 'technical' ? '600' : '400',
              cursor: 'pointer',
              borderBottom: activeTab === 'technical' ? '2px solid #3b82f6' : 'none'
            }}
          >
            ⚡ Technical Guide
          </button>
        </div>

        {/* Content */}
        <div style={{ maxHeight: '60vh', overflow: 'auto', padding: '2rem' }}>
          {/* Steps */}
          <div style={{ marginBottom: '2rem' }}>
            {steps[activeTab].map((step, index) => (
              <div 
                key={index}
                style={{
                  display: 'flex',
                  gap: '1rem',
                  marginBottom: '2rem',
                  padding: '1.5rem',
                  backgroundColor: '#f8fafc',
                  borderRadius: '0.75rem',
                  border: '1px solid #e2e8f0'
                }}
              >
                <div 
                  style={{
                    width: '3rem',
                    height: '3rem',
                    backgroundColor: '#3b82f6',
                    color: 'white',
                    borderRadius: '50%',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 'bold',
                    flexShrink: 0
                  }}
                >
                  {step.step}
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                    <span style={{ fontSize: '1.5rem' }}>{step.icon}</span>
                    <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#1f2937', margin: 0 }}>
                      {step.title}
                    </h3>
                    <span 
                      style={{
                        padding: '0.25rem 0.5rem',
                        backgroundColor: '#dbeafe',
                        color: '#3b82f6',
                        borderRadius: '0.25rem',
                        fontSize: '0.75rem',
                        fontWeight: '500'
                      }}
                    >
                      {step.time}
                    </span>
                  </div>
                  <p style={{ color: '#4b5563', marginBottom: '0.75rem', lineHeight: '1.5' }}>
                    {step.description}
                  </p>
                  <ul style={{ color: '#6b7280', fontSize: '0.875rem', margin: 0, paddingLeft: '1rem' }}>
                    {step.details.map((detail, i) => (
                      <li key={i} style={{ marginBottom: '0.25rem' }}>{detail}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>

          {/* Troubleshooting */}
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#1f2937', marginBottom: '1rem' }}>
              🛠️ Troubleshooting
            </h3>
            {troubleshooting.map((item, index) => (
              <div 
                key={index}
                style={{
                  marginBottom: '1.5rem',
                  padding: '1rem',
                  backgroundColor: '#fef3c7',
                  borderRadius: '0.5rem',
                  border: '1px solid #f59e0b'
                }}
              >
                <h4 style={{ fontSize: '1rem', fontWeight: '600', color: '#92400e', marginBottom: '0.5rem' }}>
                  Problem: {item.problem}
                </h4>
                <ul style={{ color: '#78350f', fontSize: '0.875rem', margin: 0, paddingLeft: '1rem' }}>
                  {item.solutions.map((solution, i) => (
                    <li key={i} style={{ marginBottom: '0.25rem' }}>{solution}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>

          {/* Important Notes */}
          <div 
            style={{
              padding: '1.5rem',
              backgroundColor: '#f0fdf4',
              borderRadius: '0.75rem',
              border: '1px solid #10b981',
              marginTop: '2rem'
            }}
          >
            <h4 style={{ fontSize: '1rem', fontWeight: '600', color: '#047857', marginBottom: '0.75rem' }}>
              🔒 Important Privacy Information
            </h4>
            <ul style={{ color: '#065f46', fontSize: '0.875rem', margin: 0, paddingLeft: '1rem', lineHeight: '1.6' }}>
              <li>Your data never leaves your device - all analysis happens locally</li>
              <li>We don't store, save, or share your TikTok data anywhere</li>
              <li>Requesting your data from TikTok is completely safe and legal</li>
              <li>You can delete the downloaded file after analysis if desired</li>
              <li>This process doesn't change any of your TikTok privacy settings</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DataGuide; 