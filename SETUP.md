# 🚀 Setup Guide

Complete installation and configuration guide for Real-Time Call Center AI.

## Prerequisites

- Python 3.8+ (with `uv` recommended)
- PostgreSQL 12+ (running locally or remotely)
- Redis 6+ (running locally or remotely)
- Node.js 16+ and npm (for frontend)
- Ollama (optional, for local LLM) or OpenRouter/OpenAI API key

## Installation

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/yourusername/realtime-call-center-ai
cd realtime-call-center-ai

# Start all services
docker-compose up -d

# Initialize database
docker-compose exec api-gateway python setup_database.py

# View logs
docker-compose logs -f
```

Access:
- Frontend: http://localhost:3000
- API Gateway: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Option 2: Manual Setup

1. **Navigate to project directory**
   ```bash
   cd realtime-call-center-ai
   ```

2. **Install Python dependencies**
   ```bash
   # Using uv (recommended)
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python setup_database.py
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

   # Option 2: Hugging Face
   # USE_OLLAMA=false
   # USE_HUGGINGFACE=true
   # HUGGINGFACE_API_KEY=your_hf_token_here
   # LLM_MODEL=meta-llama/Llama-3.2-3B-Instruct

   # Option 3: OpenRouter
   # USE_OLLAMA=false
   # OPENROUTER_API_KEY=your_key_here
   # LLM_MODEL=openai/gpt-3.5-turbo

   # Option 4: OpenAI
   # USE_OLLAMA=false
   # OPENAI_API_KEY=your_key_here
   # LLM_MODEL=gpt-4-turbo-preview

   # LLM Settings
   LLM_MAX_TOKENS=1500
   LLM_CONTEXT_CHUNKS=8
   LLM_ANALYSIS_INTERVAL=10

   # API Configuration
   API_HOST=0.0.0.0
   API_PORT=8000

   # Security (Production)
   # CORS_ORIGINS=http://localhost:3000,http://localhost:5173
   # RATE_LIMIT_PER_MINUTE=60

   # Logging
   LOG_LEVEL=INFO
   LOG_FORMAT=text
   ENVIRONMENT=development
   ```

5. **Start the services**

   ```bash
   # Terminal 1: API Gateway
   python api_gateway.py

   # Terminal 2: Streaming Processor
   python streaming_processor.py

   # Terminal 3: LLM Processor
   python llm_processor.py

   # Terminal 4: Frontend
   cd frontend
   npm install
   npm run dev
   ```

6. **Access the application**
   - Frontend: http://localhost:3000
   - API Gateway: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## LLM Provider Setup

### Ollama (Local, Recommended for Development)

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull model
ollama pull llama3.2

# Verify
curl http://localhost:11434/api/tags
```

### OpenRouter

1. Sign up at https://openrouter.ai
2. Create API key
3. Add credits
4. Set `OPENROUTER_API_KEY` in `.env`

### OpenAI

1. Get API key from https://platform.openai.com
2. Set `OPENAI_API_KEY` in `.env`

### Hugging Face

1. Get API token from https://huggingface.co/settings/tokens
2. Set `HUGGINGFACE_API_KEY` in `.env`

## Production Considerations

⚠️ **This is a demonstration application**

For production deployment, consider:

- **Authentication/Authorization**: Implement JWT or OAuth2
- **Rate Limiting**: Add middleware for API rate limiting
- **SSL/TLS**: Encrypt WebSocket connections
- **Secrets Management**: Use a secrets manager (AWS Secrets Manager, HashiCorp Vault)
- **Database**: Set up access controls, backups, and monitoring
- **Monitoring**: Add Prometheus metrics, Sentry for error tracking
- **CORS**: Restrict allowed origins in production
- **Environment**: Set `ENVIRONMENT=production` in `.env`

## Troubleshooting

### Database Connection Issues

```bash
# Check PostgreSQL is running
pg_isready -h localhost -p 5432

# Test connection
psql -h localhost -U postgres -d andela_ai_engineering_bootcamp
```

### Redis Connection Issues

```bash
# Check Redis is running
redis-cli ping

# Should return: PONG
```

### LLM Provider Issues

- **Ollama**: Ensure service is running: `ollama serve`
- **OpenRouter**: Check API key and credits
- **OpenAI**: Verify API key is valid and has credits
- **Hugging Face**: Check API token permissions

### Port Conflicts

If ports are already in use:

```bash
# Change ports in .env
API_PORT=8001
FRONTEND_PORT=3001
```

## Development Tools

- **CI/CD**: GitHub Actions for automated testing
- **Code Quality**: Black, Ruff, ESLint, Prettier
- **Testing**: pytest with coverage reporting

```bash
# Run tests
pytest

# Format code
black .
ruff check .

# Frontend linting
cd frontend
npm run lint
npm run format
```
