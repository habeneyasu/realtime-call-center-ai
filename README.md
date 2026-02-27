# 🎙️ Real-Time Call Center AI

> Transforming customer service through real-time AI—where every conversation becomes actionable intelligence.

## 📋 The Story Behind This Project

Call centers handle millions of conversations daily, but traditional systems struggle with real-time insights. Agents juggle multiple calls, supervisors can't monitor quality in real-time, and valuable information gets lost in post-call notes. What if every conversation could be **transcribed, analyzed, and summarized instantly**—giving agents and supervisors the insights they need, when they need them?

That's exactly what **Real-Time Call Center AI** does. Built as part of the **Andela AI Engineering Bootcamp** under the guidance of **ED Donner**, this project demonstrates how modern AI architecture can revolutionize customer service operations.

Instead of:
- ❌ Manual note-taking during calls
- ❌ Post-call analysis and reporting
- ❌ Missing critical information in real-time
- ❌ Delayed supervisor insights
- ❌ Lost context between handoffs

Agents and supervisors can now:
- ✅ See live transcripts as conversations happen
- ✅ Get instant AI-powered summaries and insights
- ✅ Identify customer intent and sentiment in real-time
- ✅ Extract action items automatically
- ✅ Scale processing across multiple workers seamlessly

This isn't just a demo—it's a production-ready architecture for the future of customer service.

## ✨ What It Does

Real-Time Call Center AI processes live audio conversations through a distributed, scalable pipeline:

- 🎤 **Live Audio Capture** - Browser-based audio recording with 200ms chunking
- 📝 **Real-Time Transcription** - Streaming ASR with speaker diarization
- 🧠 **Intelligent Analysis** - LLM-powered intent detection, sentiment analysis, and summarization
- 📊 **Actionable Insights** - Automatic extraction of action items, complaints, and key topics
- 🔄 **Scalable Architecture** - Redis Streams for message queuing and horizontal scaling
- 💾 **Persistent Storage** - PostgreSQL for transcript storage and analysis

## 🏗️ Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    1️⃣ FRONTEND (React)                      │
├──────────────────────────────────────────────────────────────┤
│  Agent Dashboard / Real-Time UI                               │
│  • Live audio capture (getUserMedia)                          │
│  • AudioWorklet processing (200ms chunks)                     │
│  • WebSocket client for real-time communication              │
│  • Live transcript viewer with speaker labels                │
│  • Real-time LLM insights panel                               │
└──────────────────────────────────────────────────────────────┘
               │
               │  (Bi-directional WebSocket)
               ▼
┌──────────────────────────────────────────────────────────────┐
│                2️⃣ API GATEWAY (FastAPI)                     │
├──────────────────────────────────────────────────────────────┤
│  • WebSocket endpoint (/ws/call)                             │
│  • Session management (call_id, agent_id)                    │
│  • Audio chunk ingestion                                      │
│  • Redis Stream integration                                   │
│  • LLM updates broadcasting                                   │
└──────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────┐
│               3️⃣ MESSAGE QUEUE (Redis Streams)              │
├──────────────────────────────────────────────────────────────┤
│  • Decouples ingestion from processing                        │
│  • Handles traffic spikes gracefully                          │
│  • Enables horizontal scaling                                 │
│  • Provides retry and error handling                          │
└──────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────┐
│              4️⃣ STREAMING PROCESSOR                         │
├──────────────────────────────────────────────────────────────┤
│  • Voice Activity Detection (VAD)                             │
│  • Streaming ASR (Faster-Whisper)                            │
│  • Speaker Diarization                                        │
│  • Real-time transcript generation                            │
└──────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────┐
│           5️⃣ DATABASE (PostgreSQL)                           │
├──────────────────────────────────────────────────────────────┤
│  • Immediate transcript persistence                           │
│  • Structured data storage                                    │
│  • Query and analytics support                                │
└──────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────┐
│              6️⃣ LLM PROCESSOR                              │
├──────────────────────────────────────────────────────────────┤
│  • Running summary generation                                 │
│  • Intent detection                                           │
│  • Complaint classification                                   │
│  • Action item extraction                                     │
│  • Sentiment analysis                                         │
└──────────────────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────┐
│            7️⃣ REAL-TIME DASHBOARD                          │
├──────────────────────────────────────────────────────────────┤
│  • Live transcript updates                                    │
│  • Dynamic summary refresh                                    │
│  • Intent and sentiment indicators                            │
│  • Action items panel                                         │
└──────────────────────────────────────────────────────────────┘
```

## 🚀 Key Features

### 🎯 Real-Time Processing

- **Streaming Transcription**: Audio-to-text conversion as conversations happen
- **Live Updates**: WebSocket-based real-time dashboard updates
- **Low Latency**: Sub-second processing pipeline for immediate insights
- **Speaker Diarization**: Automatic speaker identification and labeling

### 🤖 AI-Powered Analysis

- **Intent Detection**: Classifies conversation intent (question, complaint, request, etc.)
- **Sentiment Analysis**: Real-time emotion and tone detection
- **Complaint Classification**: Identifies and categorizes complaints with severity levels
- **Action Item Extraction**: Automatically extracts tasks and follow-ups
- **Running Summaries**: Incremental summary generation as conversations progress

### 📈 Scalable Architecture

- **Redis Streams**: Message queue for decoupled, scalable processing
- **Horizontal Scaling**: Support for multiple processing workers
- **Error Handling**: Comprehensive retry logic and graceful degradation
- **Resource Management**: Efficient memory and CPU usage

### 🛡️ Production-Ready

- **Database Persistence**: PostgreSQL for reliable data storage
- **WebSocket Management**: Robust connection handling and reconnection
- **Environment Configuration**: Flexible configuration via environment variables
- **Docker Support**: Complete containerization for easy deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ with `uv` installed
- PostgreSQL 12+ (running locally or remotely)
- Redis 6+ (running locally or remotely)
- Node.js 16+ and npm (for frontend)
- Ollama (optional, for local LLM) or OpenRouter/OpenAI API key

### Installation

1. **Navigate to the project directory**

   ```bash
   cd realtime-call-center-ai
   ```

2. **Install Python dependencies**

   ```bash
   # Using uv (recommended)
   uv pip install -r requirements.txt
   
   # For full features (audio processing)
   uv pip install -r requirements-full.txt
   ```

3. **Set up the database**

   ```bash
   uv run python setup_database.py
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   # Database
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_NAME=andela_ai_engineering_bootcamp

   # Redis
   REDIS_HOST=localhost
   REDIS_PORT=6379

   # LLM Configuration
   # Option 1: Ollama (Local, Open Source - recommended)
   USE_OLLAMA=true
   OLLAMA_BASE_URL=http://localhost:11434/v1
   LLM_MODEL=llama3.2

   # Option 2: Hugging Face (Local or Cloud)
   # USE_OLLAMA=false
   # USE_HUGGINGFACE=true
   # HUGGINGFACE_API_KEY=your_hf_token_here  # Optional for public models
   # HUGGINGFACE_ENDPOINT=https://api-inference.huggingface.co  # Optional custom endpoint
   # LLM_MODEL=meta-llama/Llama-3.2-3B-Instruct

   # Option 3: OpenRouter (Cloud)
   # USE_OLLAMA=false
   # USE_HUGGINGFACE=false
   # OPENROUTER_API_KEY=your_key_here
   # LLM_MODEL=openai/gpt-3.5-turbo

   # Option 4: OpenAI (Cloud)
   # USE_OLLAMA=false
   # USE_HUGGINGFACE=false
   # OPENAI_API_KEY=your_key_here
   # LLM_MODEL=gpt-4-turbo-preview

   # LLM Settings
   LLM_MAX_TOKENS=1500
   LLM_CONTEXT_CHUNKS=8
   LLM_ANALYSIS_INTERVAL=10

   # API Configuration
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

5. **Start the services**

   ```bash
   # Terminal 1: API Gateway
   uv run python api_gateway.py

   # Terminal 2: Streaming Processor
   uv run python streaming_processor.py

   # Terminal 3: LLM Processor
   uv run python llm_processor.py

   # Terminal 4: Frontend
   cd frontend
   npm install
   npm run dev
   ```

6. **Access the application**

   - Frontend: http://localhost:3000
   - API Gateway: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 🐳 Docker Deployment

For containerized deployment:

```bash
# Start all services
docker-compose up -d

# Initialize database
docker-compose exec api-gateway python setup_database.py

# View logs
docker-compose logs -f
```

See `docker-compose.yml` for full configuration.

## 📊 Database Schema

### `meeting_transcripts` Table

Stores all transcription chunks with comprehensive metadata:

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Primary key |
| `call_id` | UUID | Unique call identifier |
| `title` | VARCHAR | Call title/description |
| `original_text` | TEXT | Raw ASR transcription |
| `cleaned_text` | TEXT | Post-processed transcript |
| `speaker` | VARCHAR | Speaker label (SPEAKER_00, SPEAKER_01, etc.) |
| `chunk_index` | INTEGER | Sequential chunk number |
| `start_time` | TIMESTAMP | Chunk start time |
| `end_time` | TIMESTAMP | Chunk end time |
| `duration_seconds` | FLOAT | Chunk duration |
| `llm_summary` | JSONB | LLM-generated insights |
| `is_final` | BOOLEAN | Final processing flag |
| `created_at` | TIMESTAMP | Record creation time |
| `updated_at` | TIMESTAMP | Last update time |

## 🔧 Architecture Details

### WebSocket API

**Connection:**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/call');

// Session setup
ws.onopen = () => {
  ws.send(JSON.stringify({
    call_id: 'uuid-here',
    agent_id: 'agent-123',
    action: 'start'
  }));
};

// Send audio chunks
ws.send(audioChunkBytes); // Binary format
// or
ws.send(JSON.stringify({
  type: 'audio_chunk',
  audio_data: base64Data,
  chunk_index: 0,
  timestamp: Date.now() / 1000,
  format: 'pcm',
  sample_rate: 16000,
  channels: 1
}));
```

**LLM Updates:**
```javascript
const llmWs = new WebSocket(`ws://localhost:8000/ws/llm-updates/${callId}`);

llmWs.onmessage = (event) => {
  const update = JSON.parse(event.data);
  // update.data contains: summary, intent, sentiment, action_items, etc.
};
```

### Processing Pipeline

1. **Audio Ingestion**: Frontend captures audio → chunks to 200ms → sends via WebSocket
2. **Queue Management**: API Gateway receives chunks → pushes to Redis Stream
3. **Transcription**: Streaming processor consumes → VAD → ASR → Diarization
4. **Storage**: Transcripts saved to PostgreSQL immediately
5. **Analysis**: LLM processor reads transcripts → generates insights → publishes updates
6. **Dashboard**: Frontend receives updates via WebSocket → displays in real-time

### Why Redis Streams?

- ✅ **Decoupling**: Frontend ingestion independent of heavy AI processing
- ✅ **Scalability**: Multiple workers can process chunks in parallel
- ✅ **Reliability**: Built-in message persistence and retry mechanisms
- ✅ **Performance**: Handles traffic spikes without dropping data
- ✅ **Flexibility**: Easy to add new processing stages

## 🎨 Frontend Features

### Real-Time Dashboard

- **Live Transcript Viewer**: Auto-scrolling transcript with speaker labels and timestamps
- **Summary Panel**: Dynamic LLM-generated summaries with intent and sentiment
- **Action Items**: Interactive list with priority, assignee, and due date tracking
- **Status Indicators**: Connection status, recording state, and processing indicators
- **Modern UI**: Responsive design with smooth animations and professional styling

### Audio Controls

- One-click recording start/stop
- Visual recording indicators
- Connection status monitoring
- Error handling and recovery

## 📝 Usage Examples

### Example 1: Customer Support Call

```
Agent: "Hello, how can I help you today?"
Customer: "I'm having trouble with my account login"
Agent: "Let me help you with that..."

[Real-time Analysis]
Intent: support (confidence: 0.95)
Sentiment: neutral
Action Items: 
  - Reset customer password
  - Verify account access
```

### Example 2: Complaint Handling

```
Customer: "I'm very frustrated with the service delay"
Agent: "I apologize for the inconvenience..."

[Real-time Analysis]
Intent: complaint (confidence: 0.98)
Sentiment: negative
Complaint Type: service
Severity: high
Action Items:
  - Escalate to supervisor
  - Provide compensation
```

### Example 3: Information Request

```
Customer: "What are your business hours?"
Agent: "We're open Monday to Friday, 9 AM to 5 PM"

[Real-time Analysis]
Intent: information (confidence: 0.92)
Sentiment: positive
Key Topics: business hours, operating schedule
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | React, Vite, WebSocket API |
| **Backend** | FastAPI, Uvicorn, WebSockets |
| **Message Queue** | Redis Streams |
| **Database** | PostgreSQL, SQLAlchemy |
| **ASR** | Faster-Whisper, WebRTC VAD |
| **Diarization** | pyannote.audio (optional) |
| **LLM** | Ollama (local) / OpenRouter / OpenAI |
| **Deployment** | Docker, Docker Compose |

## 🔐 Security & Best Practices

### Current Implementation

- ✅ Environment variable management for sensitive data
- ✅ SQL injection prevention (parameterized queries)
- ✅ WebSocket connection validation
- ✅ Error handling and graceful degradation
- ✅ Database connection pooling
- ✅ Input validation through Pydantic models
- ✅ Security headers (X-Content-Type-Options, X-Frame-Options, etc.)
- ✅ Configurable CORS with environment variable support
- ✅ Standardized error responses
- ✅ Structured logging (JSON or text format)
- ✅ CI/CD pipeline with automated testing
- ✅ Type hints and type checking
- ✅ Code formatting and linting (Black, Ruff, ESLint, Prettier)

### Production Considerations

⚠️ **This is a demonstration application**

- Additional authentication/authorization needed for production
- Rate limiting and DDoS protection recommended (configuration ready)
- SSL/TLS encryption for WebSocket connections
- Secure API key management (secrets manager)
- Database access controls and backups
- Monitoring and alerting systems

## 📈 What's Next

### Immediate Enhancements

- [ ] User authentication and authorization
- [ ] Multi-tenant support
- [ ] Advanced analytics dashboard
- [ ] Export functionality (PDF, CSV)
- [ ] Integration with CRM systems

### Future Possibilities

- [ ] Real-time supervisor dashboard
- [ ] Automated quality scoring
- [ ] Predictive analytics for call outcomes
- [ ] Multi-language support
- [ ] Voice cloning for agent training
- [ ] Integration with telephony systems (Twilio, etc.)

## 💡 Key Learnings

Through building this project, I learned:

1. **Redis Streams are powerful** - Perfect for decoupling real-time ingestion from heavy processing
2. **WebSockets enable true real-time** - Bi-directional communication is essential for live dashboards
3. **Horizontal scaling matters** - Architecture that supports multiple workers from day one
4. **LLM integration is flexible** - Supporting local (Ollama, Hugging Face) and cloud (OpenRouter, OpenAI) options
5. **Error handling is critical** - Comprehensive retry logic keeps the system resilient
6. **User experience drives design** - Real-time updates create a compelling product

## 🌍 The Bigger Picture

This architecture pattern extends beyond call centers. The same approach works for:

- **Healthcare**: Real-time patient consultation transcription and analysis
- **Legal**: Court proceeding transcription and case analysis
- **Education**: Lecture transcription and content summarization
- **Sales**: Sales call analysis and opportunity identification
- **Compliance**: Regulatory conversation monitoring and reporting
- **Accessibility**: Real-time captioning and translation services

**Real-time AI doesn't replace human agents—it empowers them with instant insights.**

## 🤝 Contributing

This project was created as part of the **Andela AI Engineering Bootcamp**, led by **ED Donner**. This project demonstrates real-time AI architecture, distributed systems, and LLM integration in a production-ready call center application.

Feedback and contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:
1. Fork the repository
2. Install dependencies: `pip install -r requirements.txt` and `cd frontend && npm install`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes and ensure tests pass
5. Submit a pull request

### Development Tools

- **CI/CD**: GitHub Actions for automated testing
- **Code quality**: Black, Ruff, ESLint, Prettier
- **Testing**: pytest with coverage reporting

## 🙏 Acknowledgments

- **Andela AI Engineering Bootcamp** - Educational framework and program structure
- **ED Donner** - Course instructor and mentor
- **Ollama** - Open-source local LLM server
- **Hugging Face** - Open-source model hub and inference API
- **OpenRouter** - Unified API gateway for LLM access
- **OpenAI** - GPT models and API infrastructure
- **Faster-Whisper** - Efficient speech recognition
- **FastAPI** - Modern Python web framework
- **Redis** - High-performance message queuing
- **PostgreSQL** - Robust database foundation

---

<div align="center">

**For the future of customer service:** This is proof that real-time AI can transform how we understand and respond to customer conversations.

_Built with ❤️ as part of the Andela AI Engineering Bootcamp, led by ED Donner_

**Real-Time Call Center AI**

</div>
