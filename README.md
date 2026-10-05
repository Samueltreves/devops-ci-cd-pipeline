# 🚀 Enterprise CI/CD Pipeline for Microservices

![Build Status](https://github.com/Samueltreves/devops-ci-cd-pipeline/actions/workflows/ci.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/samueltreves/devops-app)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

An automated, secure, and multi-architecture CI/CD pipeline built with **GitHub Actions**, **Docker Buildx**, **Trivy**, and **Discord Webhooks**.

---

## 🏗 Pipeline Architecture
---

## 🛠 Tech Stack

| Domain | Technology |
| :--- | :--- |
| **Language & Framework** | Python 3.10, Flask, Pytest |
| **Containerization** | Docker, Docker Buildx, QEMU |
| **CI/CD Platform** | GitHub Actions |
| **Security Scanning** | Trivy (OS & Library Vulnerabilities) |
| **Registry** | Docker Hub (`samueltreves/devops-app`) |
| **Alerting** | Discord Webhooks via `curl` |

---

## 🏷 Versioning & Tagging Strategy

The pipeline supports **Semantic Versioning** and automated Docker Hub tagging:
* **`latest`**: Updated automatically on every push to the `main` branch.
* **`<SHA>`**: Short commit SHA tag generated for precise traceability.
* **`vX.Y.Z`**: Official release tags triggered automatically via Git Tags (e.g., `git tag v1.0.0`).

---

## ⚡ Quick Start

### Local Setup (WSL / Linux)
1. Clone the repository:
   ```bash
   git clone [https://github.com/Samueltreves/devops-ci-cd-pipeline.git](https://github.com/Samueltreves/devops-ci-cd-pipeline.git)
   cd devops-ci-cd-pipeline
