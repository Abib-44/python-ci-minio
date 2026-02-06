# 🐍 Python CI/CD with MinIO

![Python](https://img.shields.io/badge/python-3.12-blue)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Abib-44/python-ci-minio/python-ci-minio.yml)
![License](https://img.shields.io/badge/license-MIT-green)

Automated **Python ETL pipeline** with testing and optional deployment to **MinIO** (S3-compatible object storage).

---

## 📌 Overview

This repository provides:

- A Python 3.12 ETL workflow processing CSV files
- Unit testing using `pytest`
- CI/CD pipeline via **GitHub Actions**
- Deployment of outputs to **MinIO**

---

## 🗂 Project Structure

```
.
├── .github/workflows/        # GitHub Actions CI/CD pipeline
├── app/                      # ETL application modules
│   ├── __init__.py
│   └── etl.py                # ETL script
├── tests/                    # Unit tests
│   └── test_etl.py
├── deploy_to_minio.py        # Upload ETL output to MinIO
├── sample_input.csv          # Example input CSV
├── requirements.txt          # Python dependencies
├── pytest.ini                # Pytest configuration
├── venv/                     # Virtual environment
└── README.md                 # This file
```

## ⚙️ Setup

1. Clone the repository:

```bash
git clone https://github.com/Abib-44/python-ci-minio.git
cd python-ci-minio
