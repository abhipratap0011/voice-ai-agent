# 🧠 Voice AI Agent

> A real-time voice assistant that listens, thinks, searches the web, and speaks back — end to end in under 3 seconds.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-WebSockets-green)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3-purple)
![Whisper](https://img.shields.io/badge/STT-Whisper-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

🔗 **[Live Demo](https://huggingface.co/spaces/Abhi001999/voice-ai-agent)** &nbsp;|&nbsp; 📂 **[GitHub](https://github.com/abhipratap0011/voice-ai-agent)**

---

## 🎯 What it does

Ask anything by voice:
- *"What is the latest news in AI?"* → searches web → speaks answer
- *"What is Apple's stock price?"* → fetches live data → speaks answer
- *"Explain quantum computing"* → answers from knowledge → speaks answer
- *"Who won the IPL 2025?"* → searches web → speaks answer

No typing. No clicking. Just speak and listen.

---

## 🏗️ Architecture
Browser Mic
│  Audio chunks (WebSocket)
▼
FastAPI Backend
│
▼
faster-Whisper STT ──► Text transcript
│
▼
Groq LLaMA 3.3 70B
│         │
│    [if needed]
│         ▼
│    Tavily Web Search
│         │
│◄────────┘
▼
gTTS Text-to-Speech ──► Audio bytes (WebSocket)
│
▼
Browser Speaker

---

## ⚡ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | FastAPI + WebSockets | Real-time async server |
| STT | faster-whisper (base) | Speech to text |
| LLM | Groq LLaMA 3.3 70B | Reasoning + decisions |
| Web Search | Tavily API | Live internet access |
| TTS | gTTS | Text to speech |
| Frontend | HTML + Vanilla JS | Browser UI |
| Deployment | Docker + HuggingFace Spaces | Free hosting |

---

## 🚀 Run Locally

**Prerequisites:** Python 3.11, ffmpeg

```bash
# Clone the repo
git clone https://github.com/abhipratap0011/voice-ai-agent
cd voice-ai-agent

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your GROQ_API_KEY and TAVILY_API_KEY

# Run the server
uvicorn main:app --reload --port 8000

# Open in browser
# http://localhost:8000
```

**Free API Keys:**
- Groq → [console.groq.com](https://console.groq.com)
- Tavily → [tavily.com](https://tavily.com)

---

## 📁 Project Structure
voice-ai-agent/
├── main.py                  # FastAPI app + WebSocket server
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container for deployment
├── .env.example             # Environment variables template
├── agent/
│   ├── init.py
│   ├── stt.py               # Whisper speech-to-text
│   ├── llm.py               # Groq LLaMA + web search logic
│   ├── tools.py             # Tavily search + yFinance tools
│   ├── tts.py               # gTTS text-to-speech
│   └── memory.py            # Conversation history manager
└── frontend/
└── index.html           # Browser UI (mic + chat + audio)

---

## 🔑 Environment Variables

Create a `.env` file with:
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

---

## 🐳 Docker

```bash
docker build -t voice-ai-agent .
docker run -p 7860:7860 \
  -e GROQ_API_KEY=your_key \
  -e TAVILY_API_KEY=your_key \
  voice-ai-agent
```

---

## 💡 How It Works

1. User clicks the mic button in the browser
2. Audio is captured via `MediaRecorder` API and streamed over WebSocket
3. `faster-whisper` transcribes the audio to text locally
4. Groq LLaMA 3.3 70B processes the transcript
5. If the question needs current info — Tavily searches the web in real time
6. LLM generates a concise 2-3 sentence spoken response
7. gTTS converts the response to audio
8. Audio streams back to browser and plays automatically
9. Conversation history is maintained for context across turns

---

## 👤 Author

**Abhishek Pratap Singh**
AI Engineer · M.Tech in Artificial Intelligence, IIT Delhi
Research published at HICSS 2026

📧 abhipratapiitd@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/YOUR_PROFILE) · [GitHub](https://github.com/abhipratap0011) · [HuggingFace](https://huggingface.co/abhipratap0011)
