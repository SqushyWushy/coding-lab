import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";

import { Auth0Provider } from "@auth0/auth0-react";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Auth0Provider
      domain={import.meta.env.VITE_AUTH0_DOMAIN || "your-domain.auth0.com"}
      clientId={import.meta.env.VITE_AUTH0_CLIENT_ID || "your-client-id"}
      authorizationParams={{
        redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL || window.location.origin,
      }}
    >
      <App />
    </Auth0Provider>
  </StrictMode>,
);
