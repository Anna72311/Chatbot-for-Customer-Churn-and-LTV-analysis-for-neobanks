import React, { useState, useEffect, useRef } from 'react';
import './App.css';

const API_BASE = process.env.REACT_APP_API_URL || '';

// ── Markdown-ish renderer (bold, code blocks, tables, bullets) ──
function RenderBody({ text }) {
  const lines = text.split('\n');
  const elements = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Code block
    if (line.startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      elements.push(
        <pre key={i} className="code-block"><code>{codeLines.join('\n')}</code></pre>
      );
      i++;
      continue;
    }

    // Table
    if (line.includes('|') && line.trim().startsWith('|')) {
      const tableLines = [];
      while (i < lines.length && lines[i].includes('|') && lines[i].trim().startsWith('|')) {
        tableLines.push(lines[i]);
        i++;
      }
      const rows = tableLines.filter(l => !l.match(/^\|[-| ]+\|$/));
      elements.push(
        <div key={i} className="table-wrap">
          <table>
            <tbody>
              {rows.map((row, ri) => (
                <tr key={ri}>
                  {row.split('|').filter((_, ci) => ci > 0 && ci < row.split('|').length - 1).map((cell, ci) => (
                    ri === 0
                      ? <th key={ci}>{inlineMarkdown(cell.trim())}</th>
                      : <td key={ci}>{inlineMarkdown(cell.trim())}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
      continue;
    }

    // Bullet
    if (line.startsWith('• ') || line.startsWith('* ')) {
      const bulletLines = [];
      while (i < lines.length && (lines[i].startsWith('• ') || lines[i].startsWith('* '))) {
        bulletLines.push(lines[i].replace(/^[•*] /, ''));
        i++;
      }
      elements.push(
        <ul key={i} className="response-list">
          {bulletLines.map((b, bi) => <li key={bi}>{inlineMarkdown(b)}</li>)}
        </ul>
      );
      continue;
    }

    // Heading (bold line ending with nothing else bold-only)
    if (line.match(/^\*\*[^*]+\*\*$/)) {
      elements.push(<h4 key={i} className="section-heading">{line.replace(/\*\*/g, '')}</h4>);
      i++; continue;
    }

    // Empty line → spacer
    if (line.trim() === '') {
      elements.push(<div key={i} className="spacer" />);
      i++; continue;
    }

    elements.push(<p key={i}>{inlineMarkdown(line)}</p>);
    i++;
  }

  return <div className="response-body">{elements}</div>;
}

function inlineMarkdown(text) {
  const parts = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return parts.map((part, i) => {
    if (part.startsWith('**') && part.endsWith('**'))
      return <strong key={i}>{part.slice(2, -2)}</strong>;
    if (part.startsWith('`') && part.endsWith('`'))
      return <code key={i} className="inline-code">{part.slice(1, -1)}</code>;
    return part;
  });
}

// ── Tag chip ──
function Tag({ label }) {
  const colorMap = {
    churn: '#e74c3c22', ltv: '#2ecc7122', ml: '#3498db22',
    revenue: '#f39c1222', metrics: '#9b59b622', features: '#1abc9c22',
    data: '#34495e22', strategy: '#e67e2222', retention: '#27ae6022',
  };
  const matchKey = Object.keys(colorMap).find(k => label.includes(k));
  return (
    <span className="tag" style={{ background: matchKey ? colorMap[matchKey] : '#ffffff10' }}>
      {label}
    </span>
  );
}

// ── Message bubble ──
function MessageBubble({ msg }) {
  if (msg.role === 'user') {
    return (
      <div className="message user-message">
        <div className="bubble user-bubble">{msg.content}</div>
      </div>
    );
  }

  if (msg.loading) {
    return (
      <div className="message bot-message">
        <div className="avatar">N</div>
        <div className="bubble bot-bubble loading-bubble">
          <span className="dot" /><span className="dot" /><span className="dot" />
        </div>
      </div>
    );
  }

  return (
    <div className="message bot-message">
      <div className="avatar">N</div>
      <div className="bubble bot-bubble">
        {msg.title && <div className="response-title">{msg.title}</div>}
        <RenderBody text={msg.content} />
        {msg.tags && msg.tags.length > 0 && (
          <div className="tag-row">
            {msg.tags.map((t, i) => <Tag key={i} label={t} />)}
          </div>
        )}
      </div>
    </div>
  );
}

// ── Topic chip ──
function TopicChip({ topic, onClick }) {
  return (
    <button className="topic-chip" onClick={() => onClick(topic)}>
      {topic.label}
    </button>
  );
}

// ── Main App ──
export default function App() {
  const [messages, setMessages] = useState([
    {
      id: 0, role: 'bot',
      title: 'NeoBank Churn & LTV Intelligence',
      content: "Welcome! I'm your specialist guide for **customer churn and lifetime value (LTV) prediction** in neobanks.\n\nSelect a topic below or ask me anything — from model selection to retention tactics.",
      tags: []
    }
  ]);
  const [topics, setTopics] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const bottomRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    fetch(`${API_BASE}/api/topics`)
      .then(r => r.json())
      .then(d => setTopics(d.topics || []))
      .catch(() => setTopics([]));
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function sendMessage(text) {
    if (!text.trim() || loading) return;
    const userMsg = { id: Date.now(), role: 'user', content: text };
    const loadingMsg = { id: Date.now() + 1, role: 'bot', loading: true };
    setMessages(prev => [...prev, userMsg, loadingMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      });
      const data = await res.json();
      setMessages(prev => [
        ...prev.filter(m => !m.loading),
        {
          id: Date.now() + 2,
          role: 'bot',
          title: data.title,
          content: data.body,
          tags: data.tags || []
        }
      ]);
    } catch {
      setMessages(prev => [
        ...prev.filter(m => !m.loading),
        { id: Date.now() + 2, role: 'bot', title: 'Error', content: 'Could not reach the server. Make sure the Python backend is running on port 5000.', tags: [] }
      ]);
    }
    setLoading(false);
    inputRef.current?.focus();
  }

  function handleTopicClick(topic) {
    setSidebarOpen(false);
    sendMessage(topic.id);
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(input);
    }
  }

  const SUGGESTED_STARTERS = [
    "What is customer churn?",
    "How do I calculate LTV?",
    "Which ML models work best?",
    "How does churn impact revenue?"
  ];

  return (
    <div className="app">
      {/* Sidebar */}
      <aside className={`sidebar ${sidebarOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <span className="sidebar-title">Topics</span>
          <button className="close-btn" onClick={() => setSidebarOpen(false)}>✕</button>
        </div>
        <div className="sidebar-topics">
          {topics.map(t => (
            <button key={t.id} className="sidebar-topic-btn" onClick={() => handleTopicClick(t)}>
              {t.label}
            </button>
          ))}
        </div>
      </aside>
      {sidebarOpen && <div className="overlay" onClick={() => setSidebarOpen(false)} />}

      {/* Main */}
      <div className="main">
        {/* Header */}
        <header className="header">
          <button className="menu-btn" onClick={() => setSidebarOpen(true)}>
            <span /><span /><span />
          </button>
          <div className="header-brand">
            <div className="logo-dot" />
            <span className="brand-name">NeoBank Intelligence</span>
          </div>
          <div className="header-badge">Churn · LTV · Retention</div>
        </header>

        {/* Chat area */}
        <div className="chat-area">
          {messages.map(msg => <MessageBubble key={msg.id} msg={msg} />)}
          <div ref={bottomRef} />
        </div>

        {/* Topic chips */}
        <div className="chips-bar">
          {topics.slice(0, 6).map(t => (
            <TopicChip key={t.id} topic={t} onClick={handleTopicClick} />
          ))}
        </div>

        {/* Starter prompts (only show initially) */}
        {messages.length <= 1 && (
          <div className="starters">
            {SUGGESTED_STARTERS.map((s, i) => (
              <button key={i} className="starter-btn" onClick={() => sendMessage(s)}>{s}</button>
            ))}
          </div>
        )}

        {/* Input */}
        <div className="input-bar">
          <textarea
            ref={inputRef}
            className="chat-input"
            rows={1}
            placeholder="Ask about churn signals, LTV formulas, ML models…"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button
            className={`send-btn ${loading ? 'sending' : ''}`}
            onClick={() => sendMessage(input)}
            disabled={loading || !input.trim()}
          >
            {loading ? '…' : '↑'}
          </button>
        </div>
      </div>
    </div>
  );
}
