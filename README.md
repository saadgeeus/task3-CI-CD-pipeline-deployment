# 🚀 Django Todo — Multi-Stage CI/CD Deployment Pipeline

A Django Todo application integrated with a multi-stage automated CI/CD pipeline using **GitHub Actions, Docker, Ruff, Django Unit Tests, and DockerHub**.

This project demonstrates an automated workflow that validates source code, runs tests, builds a Docker image, publishes versioned images to DockerHub, creates Git version tags, and generates deployment metrics through GitHub Actions.

---

## 📌 Project Overview

The objective of this project is to implement a reliable CI/CD pipeline that automatically runs whenever new code is pushed to the `main` branch.

### Pipeline Flow

```text
Developer Push
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ├── Checkout Source Code
      │
      ├── Build CI Docker Image
      │
      ├── Ruff Static Code Analysis
      │
      ├── Django Unit Tests
      │
      ├── Read Application Version
      │
      ├── Docker Image Build
      │
      ├── DockerHub Authentication
      │
      ├── Push Versioned Docker Image
      │
      ├── Push Latest Docker Image
      │
      ├── Create Git Version Tag
      │
      └── Deployment Summary & Metrics
```

---

## 🛠️ Technologies Used

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| Python              | Application programming        |
| Django 2.2.7        | Web framework                  |
| Docker              | Application containerization   |
| GitHub              | Source code repository         |
| GitHub Actions      | CI/CD automation               |
| Ruff                | Static code analysis / linting |
| Django TestCase     | Unit testing                   |
| DockerHub           | Container image registry       |
| Git Tags            | Application versioning         |
| GitHub Step Summary | Pipeline execution metrics     |
| SQLite              | Development database           |
| Gunicorn            | WSGI application server        |

---

## 📂 Project Structure

```text
task3-CI-CD-pipeline-deployment/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── todoApp/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── todos/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── staticfiles/
├── volume/
├── manage.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── ruff.toml
├── VERSION
└── README.md
```

---

# 🔄 CI/CD Pipeline Stages

## 1. Checkout Source Code

GitHub Actions automatically checks out the latest source code from the `main` branch.

```yaml
- name: Checkout source code
  uses: actions/checkout@v4
```

---

## 2. Build CI Docker Image

The pipeline builds a Docker image containing the application and its required dependencies.

```bash
docker build -t django-todo:ci .
```

This provides a consistent environment for linting and testing.

---

## 3. Static Code Analysis

Ruff is used to perform automated static code analysis.

```bash
docker run --rm django-todo:ci ruff check .
```

The pipeline stops if linting fails.

### Ruff Configuration

The project uses the following checks:

```text
E - pycodestyle errors
F - Pyflakes checks
I - Import sorting
```

Django migration files are excluded from the linting process.

---

## 4. Unit Testing

Django's built-in testing framework executes the application test suite.

```bash
docker run --rm django-todo:ci python manage.py test
```

Current test coverage includes:

* Todo model creation
* Todo string representation
* Todo index view
* Adding a Todo
* Updating a Todo
* Deleting a Todo

### Current Test Result

```text
Ran 6 tests

OK
```

---

# 🐳 Docker Containerization

The application uses a Python 3.8 Docker base image because the project is based on Django 2.2.7.

### Docker Image

```text
saadgeeus/django-todo
```

The application runs with Gunicorn:

```bash
gunicorn --bind 0.0.0.0:8000 todoApp.wsgi:application
```

---

# 📦 Versioning Strategy

Application versions are controlled through the `VERSION` file.

Example:

```text
1.0.0
```

The CI/CD pipeline converts this into:

```text
v1.0.0
```

### Docker Image Tags

```text
saadgeeus/django-todo:v1.0.0
saadgeeus/django-todo:latest
```

For the next release, update:

```text
1.0.0
```

to:

```text
1.0.1
```

The next pipeline execution will publish:

```text
saadgeeus/django-todo:v1.0.1
saadgeeus/django-todo:latest
```

The pipeline also creates the corresponding Git tag:

```text
v1.0.1
```

---

# 🔐 DockerHub Authentication

DockerHub credentials are not stored inside the source code.

GitHub Actions repository secrets are used:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

The workflow authenticates securely:

```yaml
- name: DockerHub login
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
```

---

# 📊 GitHub Actions Deployment Summary

After a successful pipeline execution, GitHub Actions generates an execution summary using:

```text
$GITHUB_STEP_SUMMARY
```

The summary reports:

* Branch
* Application version
* Docker image
* Latest image tag
* Lint status
* Unit test status
* Docker build status
* DockerHub push status
* Git version tag

### Example

```text
CI/CD Deployment Summary

Branch          main
Version         v1.0.0
Docker Image    saadgeeus/django-todo:v1.0.0
Latest Tag      saadgeeus/django-todo:latest
Lint            Passed
Unit Tests      Passed
Docker Build    Passed
DockerHub Push  Passed
Git Version Tag v1.0.0
```

---

# 🚀 How the Pipeline is Triggered

The pipeline automatically runs when code is pushed to:

```text
main
```

Example:

```bash
git add .
git commit -m "Update Todo application"
git push origin main
```

GitHub Actions then automatically starts the CI/CD workflow.

The workflow can also be started manually using:

```text
workflow_dispatch
```

from GitHub Actions.

---

# 🧪 Run the Project Locally

## Clone Repository

```bash
git clone https://github.com/saadgeeus/task3-CI-CD-pipeline-deployment.git
cd task3-CI-CD-pipeline-deployment
```

## Build Docker Image

```bash
docker build -t django-todo:v1.0.0 .
```

## Run Unit Tests

```bash
docker run --rm django-todo:v1.0.0 python manage.py test
```

## Run Ruff

```bash
docker run --rm django-todo:v1.0.0 ruff check .
```

## Run Application

```bash
docker run --rm -p 8000:8000 django-todo:v1.0.0
```

Then open:

```text
http://localhost:8000
```

---

# 🏗️ Dockerfile

The application is packaged using Docker with:

* Python runtime
* Django
* Gunicorn
* Ruff
* Application source code

Example build:

```bash
docker build -t django-todo:v1.0.0 .
```

---

# 🔁 Complete CI/CD Lifecycle

```text
Code Change
    │
    ▼
git push origin main
    │
    ▼
GitHub Actions Trigger
    │
    ▼
Checkout
    │
    ▼
Docker CI Environment
    │
    ├───────────────┐
    ▼               ▼
Ruff Lint       Unit Tests
    │               │
    └───────┬───────┘
            │
            ▼
       Quality Gate
            │
            ▼
       Docker Build
            │
            ▼
      DockerHub Login
            │
            ▼
   Push Versioned Image
            │
            ├── v1.0.0
            │
            └── latest
            │
            ▼
      Git Version Tag
            │
            ▼
   GitHub Actions Summary
```

---

# 🎯 Task Requirements Covered

This project fulfills the following CI/CD requirements:

* ✅ Automated remote-push workflow
* ✅ GitHub Actions automation
* ✅ Source code checkout
* ✅ Static application linting
* ✅ Automated unit testing
* ✅ Docker image build
* ✅ DockerHub container registry
* ✅ Version-wise Docker images
* ✅ Git version tagging
* ✅ Secure DockerHub credentials
* ✅ Automated execution status
* ✅ GitHub Actions deployment metrics
* ✅ Pipeline execution summary

---

# 📌 Repository Links

### GitHub Repository

https://github.com/saadgeeus/task3-CI-CD-pipeline-deployment

### DockerHub Repository

https://hub.docker.com/r/saadgeeus/django-todo

---

# 👨‍💻 Author

**Saad Khan**

DevOps / Cloud / CI/CD Learning Project

### Focus Areas

```text
Docker
GitHub Actions
CI/CD
AWS
Linux
Kubernetes
Cloud Automation
Infrastructure Automation
```

---

## 📜 License

This project is intended for educational and Progree Intern Taask.
