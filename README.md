# 🧩 Python Quality Pipeline

This repository aims to **standardize Python scripts**, **automate code validation**, and **enable continuous integration (CI/CD)** for data and software projects.  
It ensures consistency, readability, and quality across all codebases.


## 🚀 Overview

The **Python Quality Pipeline** automates:
- Linting and code style enforcement  
- Import sorting and formatting  
- Static type validation  
- Unit testing and coverage reports  
- Continuous integration through GitHub Actions

## 🧱 Stack

| Purpose | Tool | Description |
|----------|------|-------------|
| Code Style | **Black** | Enforces consistent code formatting |
| Imports | **Isort** | Automatically sorts and organizes imports |
| Linting | **Flake8** | Detects syntax errors and style issues |
| Testing | **Pytest** | Runs automated tests |
| Data Validation | **Pydantic** | Provides type-safe validation for configurations and data models |
| CI/CD | **GitHub Actions** | Runs the entire pipeline automatically on each commit or pull request |

## 🧪 Features

- Automatic code style checks before merging  
- Static analysis and linting via pre-commit hooks  
- Unit tests triggered in CI/CD pipelines  
- Enforced conventions (PEP8, typing, formatting)  
- Clear structure for scalable Data Engineering and Python projects  

## 🧭 Goals

- Establish a common development standard for all Python scripts
- Automate code validation, testing, and formatting
- Enable consistent CI/CD integration across teams (offshore and compliance)

## 📁 Project Structure

```
.
├── .github/
├── .flake8
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── README.md
├── src/
│   ├── collectors/
│   │   ├── __init__.py
│   │   ├── base_collector.py
│   │   └── coingecko_collector.py
│   ├── validators/
│   │   ├── __init__.py
│   │   └── data_schemas.py (Pydantic models)
│   ├── processors/
│   │   ├── __init__.py
│   │   └── data_processor.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── test_collectors.py
│   └── test_validators.py
└── data/
    ├── raw/
    └── processed/
```

## Useful links

- [Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [Pydantic](https://docs.pydantic.dev/latest/)
