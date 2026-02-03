# Probability Practice CLI

Generate probability practice quizzes and Jupyter notebooks from topic question banks.

## Requirements

- Python 3.11+
- `nbformat` installed
- `OPENROUTER_API_KEY` set in your environment (for solution generation)

## Quick Start

```bash
uv run python probability-practice/main.py \
  --topics combinations permutations \
  --difficulty easy \
  --count 5 \
  --quizzes-dir probability-practice/quizzes \
  --notebooks-dir probability-practice/notebooks
```

This will:
1. Randomly select and enrich questions by topic.
2. Generate solutions via OpenRouter.
3. Write a quiz JSON file to the quizzes directory.
4. Write a notebook to the notebooks directory.

## CLI Options

- `--topics` (required): One or more topic names (e.g., `combinations permutations probability_axioms`)
- `--difficulty`: `easy`, `medium`, or `hard`
- `--count`: Number of questions (default: 10)
- `--quizzes-dir`: Output directory for quiz JSON files
- `--notebooks-dir`: Output directory for generated notebooks
- `--seed`: Optional random seed
- `--model`: Optional OpenRouter model override
- `--timeout`: OpenRouter request timeout in seconds (default: 60)
- `--title`: Optional notebook title override

## Quiz JSON Format

```json
{
  "metadata": {
    "topics": ["combinations"],
    "difficulty": "easy",
    "count": 5,
    "generated_at": "02_03_2026_14_22_10"
  },
  "questions": [
    {
      "question": "How many ways to ...",
      "solution-template": "",
      "difficulty": "easy",
      "topic": "combinations",
      "solution": "Step-by-step solution..."
    }
  ]
}
```

## Notebook Generation Only

You can generate a notebook directly from a quiz JSON file:

```bash
python probability-practice/src/generate_notebook.py \
  --quiz probability-practice/quizzes/sample.json \
  --output-dir probability-practice/notebooks
```
