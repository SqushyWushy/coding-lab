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
        description: "Tap the 'Profile' icon at the bottom right of your screen",
        details: [
          "Look for the person icon in the bottom navigation bar",
          "This will take you to your personal profile page",
          "You should see your profile picture, bio, and follower count"
        ],
        icon: "👤",
        time: "10 seconds"
      },
      {
        step: 3,
        title: "Open the Menu",
        description: "Tap the three horizontal lines (☰) in the top right corner",
        details: [
          "This is called the 'hamburger menu'",
          "It's located in the top-right corner of your profile page",
          "If you can't see it, make sure you're on your own profile page"
        ],
        icon: "☰",
        time: "10 seconds"
      },
      {
        step: 4,
        title: "Open Settings and Privacy",
        description: "Scroll down and tap 'Settings and privacy'",
        details: [
          "It's usually located towards the bottom of the menu",
          "This option controls all your TikTok settings",
          "Don't worry - we're just accessing your data download options"
        ],
        icon: "🔒",
        time: "15 seconds"
      },
      {
        step: 5,
        title: "Go to Account Settings",
        description: "Tap on 'Account' in the settings menu",
        details: [
          "This section contains your account management options",
          "Look for it near the top of the Settings and privacy page",
          "This is where TikTok keeps data download options"
        ],
        icon: "👤",
        time: "10 seconds"
      },
      {
        step: 6,
        title: "Find Download Your Data",
        description: "Scroll down and tap 'Download your data'",
        details: [
          "This option may be located under account management features",
          "TikTok is legally required to provide this option",
          "It's completely free and safe to use"
        ],
        icon: "📥",
        time: "20 seconds"
      },
      {
        step: 7,
        title: "Request Data Tab",
        description: "You'll see the 'Request data' tab is already selected",
        details: [
          "All data categories are chosen by default - that's perfect!",
          "You don't need to change what data to include",
          "We just need to change the file format in the next step"
        ],
        icon: "📋",
        time: "5 seconds"
      },
      {
        step: 8,
        title: "Choose JSON Format",
        description: "Change the file format from TXT to JSON",
        details: [
          "Look for 'Select file format' option",
          "Make sure to select 'JSON' NOT 'TXT'",
          "JSON format is required for our analysis tool to work",
          "TXT files won't work with our app"
        ],
        icon: "📄",
        time: "15 seconds"
      },
      {
        step: 9,
        title: "Submit Your Request",
        description: "Tap 'Request data' to submit your download request",
        details: [
          "TikTok will start processing your data",
          "You'll see a confirmation that your request was submitted",
          "Processing typically takes a few hours to several days"
        ],
        icon: "✅",
        time: "10 seconds"
      },
      {
        step: 10,
        title: "Wait for Processing",
        description: "TikTok will process your request (this may take some time)",
        details: [
          "You'll get a notification when your data is ready",
          "Processing time varies but usually takes 1-7 days",
          "You can check the status by returning to the same page",
          "Don't submit multiple requests - just be patient"
        ],
        icon: "⏱️",
        time: "1-7 days"
      },
      {
        step: 11,
        title: "Download Your Data",
        description: "Return to 'Download your data' and switch to the 'Download data' tab",
        details: [
          "Go back to: Profile → Menu → Settings and privacy → Account → Download your data",
          "Click on the 'Download data' tab (not 'Request data')",
          "You should see your completed data package",
          "Tap 'Download' to get your JSON file"
        ],
        icon: "💾",
        time: "2 minutes"
      },
      {
        step: 12,
        title: "Save and Use Your File",
        description: "Your TikTok data file is now ready to upload to our analyzer!",
        details: [
          "The file will be named something like 'user_data_tiktok.json'",
          "Save it somewhere easy to find (like your Downloads folder)",
          "Come back to our app and upload this file",
          "The file contains all your TikTok activity and engagement data"
        ],
        icon: "🎉",
        time: "1 minute"
      }
    ],
    technical: [
      {
        step: 1,
        title: "Navigate to TikTok Account Settings",
        description: "Access via: Profile → Menu → Settings and privacy → Account → Download your data",
        details: [
          "Correct path: TikTok App → Profile Tab → ☰ Menu → Settings and privacy → Account",
          "Alternative: TikTok Web → Settings → Privacy and Safety → Download your data",
          "Note: Mobile app path goes through Account, not Privacy section"
        ],
        icon: "🔧",
        time: "1 minute"
      },
      {
        step: 2,
        title: "Configure Data Export Parameters",
        description: "In 'Request data' tab: Select JSON format, keep all data categories selected",
        details: [
          "Format: JSON (required for our parser)",
          "Data types: All categories selected by default (recommended)",
          "Date range: All available data (no date filtering needed)",
          "File structure will be nested JSON with activity categories"
        ],
        icon: "⚙️",
        time: "30 seconds"
      },
      {
        step: 3,
        title: "Submit GDPR/CCPA Data Request",
        description: "Initiate formal data portability request via 'Request data' button",
        details: [
          "Request type: Data portability under GDPR Article 20",
          "Processing time: 1-7 days (varies by data volume and server load)",
          "Legal basis: User data subject rights",
          "Status tracking: Available in same interface"
        ],
        icon: "📋",
        time: "Instant"
      },
      {
        step: 4,
        title: "Monitor Processing Status",
        description: "Check 'Download data' tab for completion status",
        details: [
          "Status updates: Available in-app (no email notifications by default)",
          "Processing indicators: Pending → Processing → Ready for download",
          "Access method: Return to Account → Download your data → Download data tab",
          "Refresh frequency: Check daily until ready"
        ],
        icon: "⏱️",
        time: "1-7 days"
      },
      {
        step: 5,
        title: "Download & Validate Data Package",
        description: "Retrieve data from 'Download data' tab and verify integrity",
        details: [
          "File format: JSON (user_data_tiktok.json, ~1-50MB depending on activity)",
          "Download method: Direct download from Download data tab",
          "Structure: Nested objects with Activity, Profile, Video interactions",
          "Validation: Ensure file is valid JSON and >1KB in size"
        ],
        icon: "📦",
        time: "2 minutes"
      }
    ]
  };

  const troubleshooting = [
    {
      problem: "Can't find 'Download your data' option",
      solutions: [
        "Update your TikTok app to the latest version",
        "Make sure you're looking in Account settings, not Privacy settings",
        "Check if the feature is available in your region",
        "Try restarting the app and following the path again"
      ]
    },
    {
      problem: "Data request is taking too long",
      solutions: [
        "Wait up to 7 days - processing can be slow",
        "Check the 'Download data' tab regularly for status updates",
        "Don't submit multiple requests - this can delay processing",
        "If it's been over a week, try requesting again"
      ]
    },
    {
      problem: "Can't find the Download data tab",
      solutions: [
        "Make sure you're in Account → Download your data",
        "Look for tabs at the top: 'Request data' and 'Download data'",
        "The Download data tab only appears after you've made a request",
        "Try refreshing by going back and entering the section again"
      ]
    },
    {
      problem: "File is not in JSON format",
      solutions: [
        "Make sure you selected JSON (not TXT) when requesting",
        "If you have a TXT file, you'll need to request again with JSON format",
        "Check that the file extension is .json",
        "The file should start with { and end with } when opened in a text editor"
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