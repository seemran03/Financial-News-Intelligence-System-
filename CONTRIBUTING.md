# Contributing to Financial News Intelligence System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository** (if applicable)
2. **Clone your fork** or the repository
3. **Set up development environment:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and modular

### Adding New Features

#### Adding a New Agent
1. Create a new file in `src/agents/`
2. Implement the agent class with a `__call__` method
3. Add the agent to `src/agents/__init__.py`
4. Integrate into `src/workflow.py`
5. Add tests in `tests/`

#### Extending Entity Extraction
- Add new entity types to `src/models.py`
- Update `EntityExtractionAgent` with extraction logic
- Add keywords/patterns to `config.py`

#### Adding Stock Symbols
- Update `STOCK_SYMBOLS_MAPPING` in `config.py`
- Add sector mappings if needed

## 🧪 Testing

Run tests with:
```bash
python -m pytest tests/
```

Or use unittest:
```bash
python -m unittest tests.test_agents
```

## 📚 Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update this file if contributing guidelines change

## 🐛 Reporting Issues

When reporting issues, please include:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)

## ✨ Feature Requests

Feature requests are welcome! Please describe:
- The feature you'd like to see
- Use case or problem it solves
- Any implementation ideas (optional)

## 🔄 Pull Request Process

1. Create a feature branch
2. Make your changes
3. Add/update tests
4. Update documentation
5. Ensure all tests pass
6. Submit pull request with clear description

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Happy coding! 🎉


