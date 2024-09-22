import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { AuthProvider } from "@propelauth/react";
import { BrowserRouter } from "react-router-dom";
import { propelAuthURL } from '../config.jsx';
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <AuthProvider authUrl={propelAuthURL}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </AuthProvider>
  </StrictMode>
)
