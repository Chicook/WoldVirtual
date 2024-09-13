// BK_React/src/index.jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

export const renderReactComponent = () => {
  ReactDOM.render(<App />, document.getElementById('react-root'));
  };
  