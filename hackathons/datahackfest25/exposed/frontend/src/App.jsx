import { useState } from 'react';
import { useAuth0 } from "@auth0/auth0-react";
import Dashboard from "./pages/Dashboard.jsx";
import DataGuide from "./components/DataGuide.jsx";

function App() {
  const { loginWithRedirect, logout, user, isAuthenticated, isLoading } = useAuth0();
  const [showLogin, setShowLogin] = useState(false);
  const [loginData, setLoginData] = useState({ email: '', password: '' });
  const [showDataGuide, setShowDataGuide] = useState(false);

  // Check if Auth0 is properly configured
  const auth0Configured = import.meta.env.VITE_AUTH0_DOMAIN && 
                         import.meta.env.VITE_AUTH0_CLIENT_ID && 
                         import.meta.env.VITE_AUTH0_DOMAIN !== "your-domain.auth0.com";

  // For hackathon demo, prioritize demo mode to avoid Auth0 dev key issues
  const preferDemo = true;

  const handleLogin = () => {
    if (auth0Configured) {
      loginWithRedirect();
    } else {
      setShowLogin(true);
    }
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();
    if (loginData.email && loginData.password) {
      setShowLogin(false);
      // Don't show alert, just proceed to dashboard
    } else {
      alert('Please fill in both email and password');
    }
  };

  const handleLogout = () => {
    if (auth0Configured) {
      logout({ returnTo: window.location.origin });
    } else {
      setLoginData({ email: '', password: '' });
    }
  };

  // Show Dashboard if user is authenticated OR if demo login is complete
  if (isAuthenticated || (loginData.email && !showLogin)) {
    return <Dashboard />;
  }

  if (isLoading) {
    return (
      <div 
        style={{
          minHeight: '100vh',
          background: 'linear-gradient(135deg, #f9fafb 0%, #e0f2fe 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
        }}
      >
        <div style={{ textAlign: 'center' }}>
          <div 
            style={{
              width: '40px',
              height: '40px',
              border: '4px solid #e5e7eb',
              borderTop: '4px solid #3b82f6',
              borderRadius: '50%',
              animation: 'spin 1s linear infinite',
              margin: '0 auto 1rem'
            }}
          />
          <p style={{ color: '#6b7280' }}>Loading...</p>
        </div>
      </div>
    );
  }

  if (showLogin && !auth0Configured) {
    return (
      <div 
        style={{
          minHeight: '100vh',
          background: 'linear-gradient(135deg, #f9fafb 0%, #e0f2fe 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
        }}
      >
        <div 
          style={{
            backgroundColor: 'white',
            padding: '3rem',
            borderRadius: '1rem',
            boxShadow: '0 20px 40px rgba(0,0,0,0.1)',
            width: '100%',
            maxWidth: '400px',
            margin: '2rem'
          }}
        >
          <h2 
            style={{
              fontSize: '1.5rem',
              fontWeight: '600',
              color: '#111827',
              textAlign: 'center',
              marginBottom: '1rem'
            }}
          >
            Login to EXPOSED
          </h2>
          
          <p 
            style={{
              fontSize: '0.875rem',
              color: '#6b7280',
              textAlign: 'center',
              marginBottom: '2rem'
            }}
          >
            Demo mode - Auth0 not configured
          </p>
          
          <form onSubmit={handleLoginSubmit}>
            <div style={{ marginBottom: '1.5rem' }}>
              <label 
                style={{
                  display: 'block',
                  fontSize: '0.875rem',
                  fontWeight: '500',
                  color: '#374151',
                  marginBottom: '0.5rem'
                }}
              >
                Email
              </label>
              <input
                type="email"
                value={loginData.email}
                onChange={(e) => setLoginData({...loginData, email: e.target.value})}
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.5rem',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3b82f6'}
                onBlur={(e) => e.target.style.borderColor = '#d1d5db'}
                placeholder="Enter your email"
              />
            </div>
            
            <div style={{ marginBottom: '2rem' }}>
              <label 
                style={{
                  display: 'block',
                  fontSize: '0.875rem',
                  fontWeight: '500',
                  color: '#374151',
                  marginBottom: '0.5rem'
                }}
              >
                Password
              </label>
              <input
                type="password"
                value={loginData.password}
                onChange={(e) => setLoginData({...loginData, password: e.target.value})}
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.5rem',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3b82f6'}
                onBlur={(e) => e.target.style.borderColor = '#d1d5db'}
                placeholder="Enter your password"
              />
            </div>
            
            <div style={{ display: 'flex', gap: '1rem' }}>
              <button
                type="submit"
                style={{
                  flex: 1,
                  padding: '0.75rem',
                  backgroundColor: '#111827',
                  color: 'white',
                  border: 'none',
                  borderRadius: '0.5rem',
                  fontSize: '1rem',
                  fontWeight: '500',
                  cursor: 'pointer'
                }}
                onMouseOver={(e) => e.target.style.backgroundColor = '#1f2937'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#111827'}
              >
                Login
              </button>
              
              <button
                type="button"
                onClick={() => setShowLogin(false)}
                style={{
                  flex: 1,
                  padding: '0.75rem',
                  backgroundColor: '#f3f4f6',
                  color: '#374151',
                  border: 'none',
                  borderRadius: '0.5rem',
                  fontSize: '1rem',
                  fontWeight: '500',
                  cursor: 'pointer'
                }}
                onMouseOver={(e) => e.target.style.backgroundColor = '#e5e7eb'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#f3f4f6'}
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div 
      style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #f9fafb 0%, #e0f2fe 100%)',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
      }}
    >
      {/* Login Button - Top Right */}
      <div style={{ display: 'flex', justifyContent: 'flex-end', padding: '2rem' }}>
        <button
          onClick={handleLogin}
          style={{
            padding: '0.5rem 1.5rem',
            backgroundColor: '#111827',
            color: 'white',
            fontSize: '0.875rem',
            fontWeight: '500',
            borderRadius: '0.5rem',
            border: 'none',
            cursor: 'pointer',
            transition: 'background-color 0.2s'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#1f2937'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#111827'}
        >
          Login
        </button>
      </div>

      {/* Main Content - Centered */}
      <div 
        style={{
          flex: 1,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '2rem'
        }}
      >
        <div 
          style={{
            textAlign: 'center',
            maxWidth: '42rem'
          }}
        >
          <h1 
            style={{
              fontSize: 'clamp(3rem, 8vw, 6rem)',
              fontWeight: '700',
              letterSpacing: '-0.025em',
              marginBottom: '1.5rem',
              background: 'linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD, #98D8C8, #F7DC6F, #FF9A9E, #A8E6CF)',
              backgroundSize: '400% 400%',
              WebkitBackgroundClip: 'text',
              backgroundClip: 'text',
              color: 'transparent',
              animation: 'tiktokGradient 6s ease infinite',
              textShadow: '0 0 30px rgba(255, 107, 107, 0.3)'
            }}
          >
            EXPOSED
          </h1>
          
          <div 
            style={{
              width: '4rem',
              height: '1px',
              backgroundColor: '#d1d5db',
              margin: '0 auto 1.5rem auto'
            }}
          ></div>
          
                           <p 
                   style={{
                     fontSize: 'clamp(1.25rem, 3vw, 1.5rem)',
                     fontWeight: '300',
                     color: '#4b5563',
                     lineHeight: '1.6',
                     marginBottom: '2rem'
                   }}
                 >
                    Transform your TikTok data into beautiful insights
                 </p>
                 
                 <button
                   onClick={() => setShowDataGuide(true)}
                   style={{
                     padding: '0.75rem 1.5rem',
                     backgroundColor: '#f3f4f6',
                     color: '#374151',
                     border: '1px solid #d1d5db',
                     borderRadius: '0.5rem',
                     fontSize: '0.875rem',
                     fontWeight: '500',
                     cursor: 'pointer',
                     display: 'inline-flex',
                     alignItems: 'center',
                     gap: '0.5rem',
                     transition: 'all 0.2s'
                   }}
                   onMouseOver={(e) => {
                     e.target.style.backgroundColor = '#e5e7eb';
                     e.target.style.transform = 'translateY(-1px)';
                   }}
                   onMouseOut={(e) => {
                     e.target.style.backgroundColor = '#f3f4f6';
                     e.target.style.transform = 'translateY(0)';
                   }}
                 >
                   <span>📥</span>
                   <span>How to Get Your TikTok Data</span>
                 </button>
          
          {!auth0Configured && (
            <div 
              style={{
                marginTop: '2rem',
                padding: '1rem',
                backgroundColor: '#fef3c7',
                border: '1px solid #f59e0b',
                borderRadius: '0.5rem',
                fontSize: '0.875rem',
                color: '#92400e'
              }}
            >
              ⚠️ Auth0 not configured. Update your .env file with Auth0 credentials.
            </div>
          )}
        </div>
      </div>

      {/* Privacy Message - Bottom */}
      <div style={{ padding: '2rem', textAlign: 'center' }}>
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
          <span>Your data is processed locally. We never store or share it. Ever.</span>
        </p>
      </div>

      {/* Data Guide Modal */}
      {showDataGuide && (
        <DataGuide onClose={() => setShowDataGuide(false)} />
      )}
    </div>
  );
}

export default App;
