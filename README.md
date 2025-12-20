# ML Gym

A practice repository for machine learning and probability concepts, experiments, and implementations.

## Purpose

This repository serves as a learning and experimentation space for:
- Machine learning concepts and algorithms
- Probability theory and statistical methods
- Implementation practice of core ML techniques
- Testing intuitions about ML fundamentals
- Experimental code and prototypes

## Setup

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Running Jupyter Notebooks

```bash
uv run jupyter notebook
```

Or for JupyterLab:
```bash
uv run jupyter lab
```

## Project Structure

```
ml_gym/
├── source/          # Main Python package
├── tests/           # Test files
├── docs/            # Documentation
├── lib/             # Ruby utilities (dual-purpose repo)
├── pyproject.toml   # Python project configuration
└── README.md        # This file
```

## Development

### Running Tests

```bash
uv run pytest
```

### Linting and Formatting

```bash
# Check code style
uv run ruff check .

# Format code
uv run ruff format .
```

### Type Checking

```bash
uv run mypy source/
```

## Dependencies

Core ML Libraries:
- NumPy: Numerical computing
- Pandas: Data manipulation and analysis
- Scikit-learn: Machine learning algorithms
- Matplotlib: Visualization
- SciPy: Scientific computing
- Jupyter: Interactive notebooks

Development Tools:
- pytest: Testing framework
- ruff: Fast linter and formatter
- mypy: Static type checking

## Note

This repository also contains Ruby code (see `lib/` and `.rb` files) as it serves dual purposes for both Python and Ruby experimentation.
