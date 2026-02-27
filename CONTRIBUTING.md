# Contributing to Real-Time Call Center AI

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

## Getting Started

1. **Fork the repository** and clone your fork
2. **Set up your development environment**:
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Set up frontend
   cd frontend
   npm install
   ```

3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Code Style

- **Python**: Follow PEP 8, use Black for formatting (line length: 100)
- **JavaScript/React**: Follow ESLint rules, use Prettier for formatting
- **Type hints**: Use type hints in Python code where possible
- **Docstrings**: Add docstrings to functions and classes

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest test_e2e.py -v
```

### Linting and Formatting

```bash
# Python
black .
ruff check .
mypy . --ignore-missing-imports

# Frontend
cd frontend
npm run lint
npm run format
```

### Code Quality Tools

The project uses:
- **Black** for Python code formatting
- **Ruff** for Python linting
- **ESLint** and **Prettier** for frontend code

## Making Changes

### Commit Messages

Follow conventional commit format:
```
type(scope): subject

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(api): add rate limiting middleware`
- `fix(websocket): handle connection timeout gracefully`
- `docs(readme): update installation instructions`

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** and code is properly formatted
4. **Create a pull request** with a clear description

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)

## Project Structure

```
.
├── api_gateway.py          # FastAPI WebSocket gateway
├── streaming_processor.py  # Audio processing worker
├── llm_processor.py        # LLM analysis worker
├── database.py             # Database models
├── models.py               # Pydantic models
├── config.py               # Configuration management
├── redis_client.py         # Redis client
├── utils/                  # Utility modules
├── frontend/               # React frontend
└── test_e2e.py            # End-to-end tests
```

## Areas for Contribution

- **Bug fixes**: Check issues labeled "bug"
- **Features**: Check issues labeled "enhancement" or "feature"
- **Documentation**: Improve README, add examples, write tutorials
- **Testing**: Add unit tests, integration tests, improve coverage
- **Performance**: Optimize code, reduce latency, improve scalability
- **Security**: Security improvements, vulnerability fixes

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Check existing issues and PRs before creating new ones

Thank you for contributing! 🎉
