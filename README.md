# redshift-fast-api

## Pre-requirement: Poetry

Poetry introduction: https://python-poetry.org/

Why poetry? All in One
- pyenv for managing python versions.
- venv for managing virtual environments (included in python3).
- pip for dependency handling, and publishing.

```bash
pip3 install poetry
```

## Update dependencies

```bash
poetry update
```

## REPL (Read-Eval-Print Loop)

```bash
# Make sure that Redshift can public access (but this is dangerous.)
# Or you need to deploy it on an EC2 instance.
uvicorn redshift_fast_api.main:app --reload --host 127.0.0.1 --port 8000
```
