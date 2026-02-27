# 📊 API Reference

WebSocket API documentation for Real-Time Call Center AI.

## WebSocket Endpoints

### `/ws/call` - Audio Ingestion

Main endpoint for receiving audio chunks from the frontend.

**Connection:**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/call');
```

**Session Setup:**
```javascript
ws.onopen = () => {
  ws.send(JSON.stringify({
    call_id: 'uuid-here',
    agent_id: 'agent-123',
    action: 'start'
  }));
};
```

**Send Audio Chunks:**

Binary format (recommended):
```javascript
ws.send(audioChunkBytes); // Raw PCM audio bytes
```

JSON format:
```javascript
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

**Control Messages:**
```javascript
// Stop recording
ws.send(JSON.stringify({
  type: 'control',
  action: 'stop'
}));

// Pause recording
ws.send(JSON.stringify({
  type: 'control',
  action: 'pause'
}));
```

**Response Messages:**
```javascript
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  switch(data.type) {
    case 'session_started':
      console.log('Session started:', data.call_id);
      break;
    case 'chunk_acknowledged':
      console.log('Chunk received:', data.chunk_index);
      break;
    case 'error':
      console.error('Error:', data.message);
      break;
  }
};
```

### `/ws/llm-updates/{call_id}` - LLM Analysis Updates

WebSocket endpoint for receiving real-time LLM analysis updates.

**Connection:**
```javascript
const llmWs = new WebSocket(`ws://localhost:8000/ws/llm-updates/${callId}`);
```

**Message Format:**
```javascript
llmWs.onmessage = (event) => {
  const update = JSON.parse(event.data);
  
  // update.data contains:
  // - summary: Running conversation summary
  // - intent: { type, confidence, description }
  // - sentiment: "positive" | "neutral" | "negative"
  // - complaint: { is_complaint, type, severity }
  // - action_items: Array of { task, priority, assignee }
  // - key_topics: Array of topics
};
```

**Example Update:**
```json
{
  "type": "llm_update",
  "call_id": "uuid-here",
  "data": {
    "summary": "Customer called about login issues. Agent provided password reset instructions.",
    "intent": {
      "type": "support",
      "confidence": 0.95,
      "description": "Technical support request"
    },
    "sentiment": "neutral",
    "complaint": {
      "is_complaint": false
    },
    "action_items": [
      {
        "task": "Reset customer password",
        "priority": "high",
        "assignee": "agent-123"
      }
    ],
    "key_topics": ["login", "password reset", "account access"]
  },
  "timestamp": 1234567890
}
```

## REST Endpoints

### `GET /` - Root Health Check

```bash
curl http://localhost:8000/
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Real-Time Call Center AI API Gateway",
  "version": "1.0.0",
  "redis_connected": true
}
```

### `GET /health` - Detailed Health Check

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "redis": {
    "connected": true,
    "stream_info": {
      "audio_chunks": 150,
      "transcript_chunks": 120
    }
  },
  "active_connections": 5,
  "active_sessions": 3
}
```

### `GET /docs` - API Documentation

Interactive Swagger/OpenAPI documentation:
```
http://localhost:8000/docs
```

## Error Responses

All errors follow a standardized format:

```json
{
  "error": "Error Type",
  "message": "Human-readable error message",
  "details": {
    "status_code": 400
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

**Common Error Codes:**
- `400` - Bad Request (invalid input)
- `401` - Unauthorized (authentication required)
- `404` - Not Found (resource doesn't exist)
- `500` - Internal Server Error
- `503` - Service Unavailable (Redis/Database down)

## Processing Pipeline

1. **Audio Ingestion**: Frontend captures audio → chunks to 200ms → sends via WebSocket
2. **Queue Management**: API Gateway receives chunks → pushes to Redis Stream
3. **Transcription**: Streaming processor consumes → VAD → ASR → Diarization
4. **Storage**: Transcripts saved to PostgreSQL immediately
5. **Analysis**: LLM processor reads transcripts → generates insights → publishes updates
6. **Dashboard**: Frontend receives updates via WebSocket → displays in real-time

## Rate Limiting

Rate limiting is configured via environment variable:
```env
RATE_LIMIT_PER_MINUTE=60
```

## Security

- All WebSocket connections are validated
- CORS is configurable via `CORS_ORIGINS` environment variable
- Security headers are automatically added to all responses
- Input validation through Pydantic models

## Testing

Use the included E2E test script:

```bash
python test_e2e.py
```

This tests:
- Health endpoints
- WebSocket connections
- Audio chunk flow
- Database persistence
- Redis streams
