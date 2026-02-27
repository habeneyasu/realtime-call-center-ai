# 🎙️ Real-Time Call Center AI

> Transforming customer service through real-time AI—where every conversation becomes actionable intelligence.

## 📋 Overview

**Real-Time Call Center AI** processes live audio conversations through a distributed, scalable pipeline—transcribing, analyzing, and summarizing in real-time. Built as part of the **Andela AI Engineering Bootcamp** under the guidance of **ED Donner**, this project demonstrates how modern AI architecture can revolutionize customer service operations.

### The Problem
Traditional call centers struggle with:
- ❌ Manual note-taking during calls
- ❌ Post-call analysis and delayed insights
- ❌ Missing critical information in real-time
- ❌ Lost context between handoffs

### The Solution
Agents and supervisors can now:
- ✅ See live transcripts as conversations happen
- ✅ Get instant AI-powered summaries and insights
- ✅ Identify customer intent and sentiment in real-time
- ✅ Extract action items automatically
- ✅ Scale processing across multiple workers seamlessly

## ✨ Key Features

- 🎤 **Live Audio Capture** - Browser-based recording with 200ms chunking
- 📝 **Real-Time Transcription** - Streaming ASR with speaker diarization
- 🧠 **Intelligent Analysis** - LLM-powered intent detection, sentiment analysis, and summarization
- 📊 **Actionable Insights** - Automatic extraction of action items, complaints, and key topics
- 🔄 **Scalable Architecture** - Redis Streams for message queuing and horizontal scaling
- 💾 **Persistent Storage** - PostgreSQL for transcript storage and analysis

## 🏗️ Architecture

```
Frontend (React) → API Gateway (FastAPI) → Redis Streams → 
  ├─ Streaming Processor (VAD, ASR, Diarization) → PostgreSQL
  └─ LLM Processor (Analysis, Summarization) → Frontend (WebSocket)
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

## 🚀 Quick Start (30 seconds)

```bash
# Clone and run (requires Docker)
git clone https://github.com/yourusername/realtime-call-center-ai
cd realtime-call-center-ai
docker-compose up -d

# Initialize database
docker-compose exec api-gateway python setup_database.py

# Open browser: http://localhost:3000
```

**For detailed setup instructions**, see [SETUP.md](SETUP.md)

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | React, Vite, WebSocket API |
| **Backend** | FastAPI, Uvicorn, WebSockets |
| **Message Queue** | Redis Streams |
| **Database** | PostgreSQL, SQLAlchemy |
| **ASR** | Faster-Whisper, WebRTC VAD |
| **Diarization** | pyannote.audio (optional) |
| **LLM** | Ollama / Hugging Face / OpenRouter / OpenAI |
| **Deployment** | Docker, Docker Compose |

## 🔐 Security & Best Practices

- ✅ Environment variable management
- ✅ SQL injection prevention
- ✅ Security headers (X-Content-Type-Options, X-Frame-Options, etc.)
- ✅ Configurable CORS
- ✅ Standardized error responses
- ✅ Structured logging
- ✅ CI/CD pipeline with automated testing

See [SETUP.md](SETUP.md) for production considerations.

## 📚 Documentation

- 📖 **[SETUP.md](SETUP.md)** - Detailed installation and configuration guide
- 📊 **[API.md](API.md)** - WebSocket API reference and examples
- 🏗️ **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture and design decisions
- 📝 **[EXAMPLES.md](EXAMPLES.md)** - Usage examples and use cases
- 🤝 **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

## 🌍 Use Cases

This architecture extends beyond call centers:
- **Healthcare**: Real-time patient consultation transcription
- **Legal**: Court proceeding transcription and analysis
- **Education**: Lecture transcription and summarization
- **Sales**: Sales call analysis and opportunity identification
- **Compliance**: Regulatory conversation monitoring

## 🤝 Contributing

This project was created as part of the **Andela AI Engineering Bootcamp**, led by **ED Donner**.

Feedback and contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🙏 Acknowledgments

- **Andela AI Engineering Bootcamp** - Educational framework and program structure
- **ED Donner** - Course instructor and mentor
- **Ollama, Hugging Face, OpenRouter, OpenAI** - LLM providers
- **Faster-Whisper, FastAPI, Redis, PostgreSQL** - Core technologies

---

<div align="center">

**Real-time AI doesn't replace human agents—it empowers them with instant insights.**

_Built with ❤️ as part of the Andela AI Engineering Bootcamp, led by ED Donner_

**Real-Time Call Center AI**

</div>
