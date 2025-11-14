# ⚙️ Python Quality Pipeline

This repository aims to **standardize Python scripts**, **automate code validation**, and **enable continuous integration (CI/CD)** for data and software projects.
It ensures consistency, readability, and quality across all codebases.

## 🚀 Overview

The **Python Quality Pipeline** automates:

- Linting and code style enforcement
- Import sorting and formatting
- Static type validation
- Unit testing and coverage reports
- Continuous integration through GitHub Actions

## 🧪 Features

| Purpose         | Tool                                                                                    | Description                                                                   |
| --------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Code Style      | [Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) | Enforces consistent code formatting                                           |
| Imports         | [isort](https://pycqa.github.io/isort/index.html)                                       | Automatically sorts and organizes imports                                     |
| Linting         | **Flake8**                                                                              | Detects syntax errors and style issues                                        |
| Git Hooks       | [pre-commit](https://pre-commit.com/)                                                   | Automates code checks (e.g., linting, formatting) before each commit          |
| Testing         | **Pytest**                                                                              | Runs automated tests                                                          |
| Data Validation | [Pydantic](https://docs.pydantic.dev/latest/)                                           | Provides type-safe validation for configurations and data models              |
| Data Quality    | [Great Expectations](https://greatexpectations.io/)                                     | Validates and documents data pipelines to ensure data quality and consistency |
| CI/CD           | **GitHub Actions**                                                                      | Runs the entire pipeline automatically on each commit or pull request         |

## 🧭 Goals

- Establish a common development standard for all Python scripts
- Automate code validation, testing, and formatting
- Enable consistent CI/CD integration across teams

## 📁 Project Structure

```
.
├── .github/
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   ├── processors/
│   │   ├── __init__.py
│   │   └── stage_randomuser.py
│   ├── validators/
│   │   ├── __init__.py
│   │   └── data_schemas.py (Pydantic models)
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── test_collectors.py
│   └── test_validators.py
└── data/
    ├── stage/
    └── processed/
```
