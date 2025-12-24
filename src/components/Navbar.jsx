import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav style={{
            borderBottom: '1px solid var(--border-color)',
            padding: '1rem 2rem',
            background: 'rgba(15, 23, 42, 0.8)',
            backdropFilter: 'blur(10px)',
            position: 'sticky',
            top: 0,
            zIndex: 100
        }}>
            <div style={{
                margin: '0 auto',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}>
                <Link to="/" style={{
                    textDecoration: 'none',
                    fontSize: '1.5rem',
                    fontWeight: 'bold',
                    background: 'linear-gradient(to right, #3b82f6, #8b5cf6)',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent'
                }}>
                    MCQ RS Aggrawal Class 9
                </Link>
            </div>
        </nav>
    );
};

export default Navbar;
