import React from 'react';
import { Link } from 'react-router-dom';
import { chapters } from '../data';

const Home = () => {
    return (
        <div className="container">
            <h1>Question Bank Chapters</h1>
            <div className="chapter-grid">
                {chapters.map((chapter) => (
                    <Link key={chapter.id} to={`/chapter/${chapter.id}`} className="chapter-card">
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                            <span style={{
                                color: 'var(--accent-color)',
                                fontSize: '0.8rem',
                                fontWeight: '600',
                                letterSpacing: '0.05em',
                                textTransform: 'uppercase'
                            }}>
                                Chapter {chapter.id}
                            </span>
                            <span style={{ color: '#64748b', fontSize: '0.85rem' }}>
                                {chapter.questions.length} Qs
                            </span>
                        </div>
                        <h3 style={{ margin: 0, fontSize: '1.2rem', color: 'var(--text-primary)' }}>{chapter.title}</h3>
                    </Link>
                ))}
            </div>
        </div>
    );
};

export default Home;
