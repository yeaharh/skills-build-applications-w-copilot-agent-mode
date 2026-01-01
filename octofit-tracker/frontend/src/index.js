import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Set REACT_APP_CODESPACE_NAME from window.location if not set
if (!process.env.REACT_APP_CODESPACE_NAME && window.location.hostname.includes('-8000.app.github.dev')) {
  const codespace = window.location.hostname.split('-8000.app.github.dev')[0];
  process.env.REACT_APP_CODESPACE_NAME = codespace;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
