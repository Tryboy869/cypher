# Contributing to CYPHER

Thank you for your interest in contributing to CYPHER!

## How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Run tests** (`pytest tests/`)
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## Development Setup

```bash
git clone https://github.com/tryboy869/cypher.git
cd cypher
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

## Reporting Issues

Please use GitHub Issues to report bugs or suggest features.

Include:
- CYPHER version
- Python version
- Operating system
- Minimal code example
- Expected vs actual behavior

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
