# MoodMap: Reddit Emotion Analyzer 🧠📊

MoodMap is an AI-powered web application that analyzes the emotional tone of Reddit posts from selected subreddits and visualizes the results. Built during a hackathon, the app leverages OpenAI and Reddit APIs to classify emotional sentiment (Joy, Sadness, Anxiety, Anger, Hope, Neutral) and display insights using interactive charts.

---

## 🚀 Features

- 🔎 Analyze emotions from any subreddit (e.g., `anxiety`, `relationships`, `mumbai`)
- 📊 Visual bar chart of emotion distribution
- 🔄 Grouped display of posts by emotion
- 🧠 Sentiment classification powered by OpenAI's GPT-4o
- 🧭 Compare 3 subreddits with emotional overlap via a (WIP) Venn Diagram
- 💬 Summary stats for quick insight

---

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Chart.js, Venn.js
- **APIs**: OpenAI (GPT-4o), Reddit (via PRAW)

---

## 🔧 Setup (Local)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/moodmap.git
cd moodmap