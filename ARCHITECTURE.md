# 🏗️ Architecture Overview

Detailed architecture documentation for Real-Time Call Center AI.

## System Architecture

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
               ├─────────────────┬─────────────────┐
               ▼                 ▼                 ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ 4️⃣ STREAMING     │  │ 5️⃣ LLM          │  │ 6️⃣ DATABASE      │
│    PROCESSOR     │  │    PROCESSOR     │  │    (PostgreSQL)  │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│ • VAD            │  │ • Summary gen   │  │ • Transcripts     │
│ • ASR            │  │ • Intent detect │  │ • Metadata        │
│ • Diarization    │  │ • Sentiment     │  │ • LLM summaries   │
└──────────────────┘  └──────────────────┘  └──────────────────┘
         │                     │
         └─────────┬───────────┘
                   ▼
         ┌──────────────────┐
         │ 7️⃣ DASHBOARD    │
         │    (Frontend)    │
         └──────────────────┘
```

## Component Details

### 1. Frontend (React)

**Responsibilities:**
- Audio capture from browser microphone
- Real-time audio chunking (200ms intervals)
- WebSocket communication with API Gateway
- Live transcript display
- LLM insights visualization

**Key Technologies:**
- React 18+ with hooks
- WebSocket API
- AudioWorklet for processing
- Vite for build tooling

### 2. API Gateway (FastAPI)

**Responsibilities:**
- WebSocket connection management
- Session validation and management
- Audio chunk ingestion
- Redis Stream integration
- LLM update broadcasting

**Key Features:**
- Security headers middleware
- CORS configuration
- Standardized error handling
- Health check endpoints

### 3. Redis Streams (Message Queue)

**Why Redis Streams?**
- ✅ **Decoupling**: Frontend ingestion independent of heavy AI processing
- ✅ **Scalability**: Multiple workers can process chunks in parallel
- ✅ **Reliability**: Built-in message persistence and retry mechanisms
- ✅ **Performance**: Handles traffic spikes without dropping data
- ✅ **Flexibility**: Easy to add new processing stages

**Streams:**
- `audio_chunks`: Raw audio data from frontend
- `transcript_chunks`: Processed transcripts ready for LLM analysis

### 4. Streaming Processor

**Pipeline:**
1. **VAD (Voice Activity Detection)**: Filters silence
2. **ASR (Automatic Speech Recognition)**: Faster-Whisper for transcription
3. **Speaker Diarization**: pyannote.audio (optional) for speaker identification
4. **Storage**: Immediate persistence to PostgreSQL
5. **Queue**: Push to LLM processing stream

**Key Features:**
- Horizontal scaling support
- Retry logic with exponential backoff
- Graceful degradation if components unavailable

### 5. LLM Processor

**Analysis Tasks:**
- Running summary generation
- Intent detection (support, complaint, information, etc.)
- Sentiment analysis (positive, neutral, negative)
- Complaint classification with severity
- Action item extraction
- Key topic identification

**LLM Providers Supported:**
- Ollama (local, open-source)
- Hugging Face (local or cloud)
- OpenRouter (unified API)
- OpenAI (cloud)

**Update Frequency:**
- Configurable via `LLM_ANALYSIS_INTERVAL` (default: 10 chunks)

### 6. Database (PostgreSQL)

**Schema:**
- `meeting_transcripts` table (see `setup_database.sql` for schema)
- JSONB storage for LLM summaries
- Indexed for fast queries
- Timestamp tracking

### 7. Real-Time Dashboard

**Features:**
- Live transcript viewer with auto-scroll
- Dynamic summary updates
- Intent and sentiment indicators
- Action items panel
- Connection status monitoring

## Data Flow

### Audio Processing Flow

```
Frontend → API Gateway → Redis Stream → Streaming Processor → Database
                                                              ↓
                                                         LLM Processor
                                                              ↓
                                                         Frontend (WebSocket)
```

### Message Flow Example

1. **User speaks** → Frontend captures audio
2. **200ms chunk** → Sent via WebSocket to API Gateway
3. **API Gateway** → Validates and pushes to Redis Stream `audio_chunks`
4. **Streaming Processor** → Consumes chunk, processes (VAD → ASR → Diarization)
5. **Database** → Transcript saved immediately
6. **Redis Stream** → Processed transcript pushed to `transcript_chunks`
7. **LLM Processor** → Consumes transcript, generates analysis
8. **WebSocket** → Analysis broadcast to frontend
9. **Frontend** → Updates dashboard in real-time

## Scalability

### Horizontal Scaling

- **API Gateway**: Stateless, can run multiple instances
- **Streaming Processor**: Multiple workers can process chunks in parallel
- **LLM Processor**: Multiple workers can analyze different calls simultaneously
- **Redis Streams**: Handles consumer groups for load distribution

### Vertical Scaling

- **Database**: Connection pooling, query optimization
- **Redis**: Memory optimization, persistence configuration
- **LLM**: Model size selection based on hardware

## Error Handling

### Retry Logic

- Exponential backoff for transient failures
- Configurable max attempts
- Graceful degradation

### Error Recovery

- Database connection pooling with auto-reconnect
- Redis connection retry
- WebSocket reconnection in frontend
- LLM provider fallback options

## Security Considerations

- **Input Validation**: Pydantic models for all inputs
- **SQL Injection**: Parameterized queries only
- **CORS**: Configurable allowed origins
- **Security Headers**: X-Content-Type-Options, X-Frame-Options, etc.
- **Environment Variables**: Sensitive data in .env (not committed)

## Performance Optimizations

- **Audio Chunking**: 200ms chunks for low latency
- **Streaming Processing**: Non-blocking async operations
- **Database Indexing**: Indexed on call_id, speaker, timestamps
- **Redis Caching**: Stream data for quick access
- **Connection Pooling**: Database and Redis connections

## Monitoring & Observability

- **Structured Logging**: JSON or text format
- **Health Checks**: `/health` endpoint with dependency status
- **Error Tracking**: Standardized error responses
- **Metrics**: Active connections, sessions, processing rates

## Future Enhancements

- Real-time supervisor dashboard
- Multi-tenant support
- Advanced analytics
- Export functionality (PDF, CSV)
- CRM integration
- Multi-language support
