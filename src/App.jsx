import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'katex/dist/katex.min.css';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Chapter from './pages/Chapter';

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ flex: 1 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chapter/:id" element={<Chapter />} />
        </Routes>
      </div>
      <footer style={{
        textAlign: 'center',
        padding: '2rem',
        color: '#64748b',
        fontSize: '0.875rem'
      }}>
        © 2025 MathMaster MCQ. Built with React & Vite.
      </footer>
    </Router>
  );
}

export default App;
