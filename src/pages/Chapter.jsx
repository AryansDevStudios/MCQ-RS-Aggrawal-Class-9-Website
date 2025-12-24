import React, { useState, useEffect, useCallback, memo } from 'react';
import { useParams, Link } from 'react-router-dom';
import Latex from 'react-latex-next';
import { chapters } from '../data';

// Memoized component to prevent re-rendering all questions when one changes
const QuestionRow = memo(({ q, isRevealed, toggleReveal, handleContextMenu }) => {
    return (
        <div className="question-row"
            onClick={() => toggleReveal(q.id)}
            onContextMenu={(e) => handleContextMenu(e, q)}
            style={{ cursor: 'pointer', userSelect: 'none' }}
        >
            <div className="q-number">{q.id}.</div>
            <div className="q-content">
                <div className="q-text">
                    <Latex>{q.question}</Latex>
                </div>
                <div className="options-grid">
                    {q.options.map((opt, i) => {
                        const isCorrect = isRevealed && i === q.answer;
                        return (
                            <div
                                key={i}
                                className="option-item"
                                style={isCorrect ? {
                                    color: '#4ade80',
                                    fontWeight: 'bold'
                                } : {}}
                            >
                                <span className="opt-label" style={isCorrect ? { color: '#4ade80' } : {}}>
                                    ({String.fromCharCode(97 + i)})
                                </span>
                                <div><Latex>{opt}</Latex></div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}, (prevProps, nextProps) => {
    return prevProps.isRevealed === nextProps.isRevealed && prevProps.q === nextProps.q;
});

const Chapter = () => {
    const { id } = useParams();
    const chapter = chapters.find(c => c.id === parseInt(id));

    const [revealed, setRevealed] = useState(new Set());
    const [contextMenu, setContextMenu] = useState(null);

    useEffect(() => {
        const handleClick = () => setContextMenu(null);
        document.addEventListener('click', handleClick);
        return () => document.removeEventListener('click', handleClick);
    }, []);

    const toggleReveal = useCallback((qId) => {
        // If clicking inside context menu, don't toggle
        setRevealed(prev => {
            const next = new Set(prev);
            if (next.has(qId)) {
                next.delete(qId);
            } else {
                next.add(qId);
            }
            return next;
        });
    }, []);

    const handleContextMenu = useCallback((e, q) => {
        e.preventDefault();

        let fullText = `Question: ${q.question}\nOptions:\n`;
        q.options.forEach((opt, i) => {
            fullText += `(${String.fromCharCode(97 + i)}) ${opt}\n`;
        });

        setContextMenu({
            x: e.pageX,
            y: e.pageY,
            text: fullText
        });
    }, []);

    const handleSearch = (engine) => {
        if (!contextMenu) return;
        const query = encodeURIComponent(contextMenu.text);
        let url = '';
        if (engine === 'google') {
            url = `https://www.google.com/search?q=${query}`;
        } else if (engine === 'chatgpt') {
            url = `https://chatgpt.com/?q=${query}`;
        }
        window.open(url, '_blank');
        setContextMenu(null);
    };

    if (!chapter) {
        return <div className="container" style={{ paddingTop: '2rem' }}>Chapter not found</div>;
    }

    return (
        <div className="container" style={{ position: 'relative' }}>
            <div style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'baseline', gap: '1rem' }}>
                <Link to="/" style={{ color: '#94a3b8', fontSize: '0.9rem' }}>&larr; Back</Link>
                <span style={{ color: '#566474' }}>|</span>
                <h1 style={{ margin: 0, fontSize: '1.5rem' }}>
                    <span style={{ color: '#94a3b8', marginRight: '0.5rem', fontWeight: 'normal' }}>Chapter {chapter.id}:</span>
                    {chapter.title}
                </h1>
            </div>

            {contextMenu && (
                <div style={{
                    position: 'absolute',
                    top: contextMenu.y,
                    left: contextMenu.x,
                    backgroundColor: '#1e293b',
                    border: '1px solid #334155',
                    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
                    borderRadius: '8px',
                    zIndex: 1000,
                    minWidth: '180px',
                    overflow: 'hidden',
                    color: '#f8fafc'
                }}>
                    <div
                        onClick={(e) => { e.stopPropagation(); handleSearch('google'); }}
                        style={{ padding: '10px 16px', cursor: 'pointer', borderBottom: '1px solid #334155', fontSize: '0.9rem' }}
                        onMouseEnter={(e) => e.target.style.backgroundColor = '#334155'}
                        onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
                    >
                        Search on Google
                    </div>
                    <div
                        onClick={(e) => { e.stopPropagation(); handleSearch('chatgpt'); }}
                        style={{ padding: '10px 16px', cursor: 'pointer', fontSize: '0.9rem' }}
                        onMouseEnter={(e) => e.target.style.backgroundColor = '#334155'}
                        onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
                    >
                        Search on ChatGPT
                    </div>
                </div>
            )}

            <div className="question-list">
                {chapter.questions.map((q) => (
                    <QuestionRow
                        key={q.id}
                        q={q}
                        isRevealed={revealed.has(q.id)}
                        toggleReveal={toggleReveal}
                        handleContextMenu={handleContextMenu}
                    />
                ))}
            </div>
        </div>
    );
};

export default Chapter;
