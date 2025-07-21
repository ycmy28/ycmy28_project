# Realtime CI/CD Pipeline for Apache Flink + Apache NiFi

This project sets up a complete CI/CD pipeline for deploying **Apache Flink** streaming jobs and **Apache NiFi** dataflows using **GitLab CI/CD**, all version-controlled and containerized with Docker Compose.

## Local Setup (via Docker Compose)

### 1️⃣ Prerequisites
- Docker & Docker Compose
- Python (for Flink job testing)
- Git + GitLab SSH access

### 2️⃣ Start the Cluster

1. **start docker compose**  
   ```bash
   docker-compose up -d
Services started:
    Flink Dashboard → http://localhost:8081
    NiFi UI → http://localhost:8080

2. **To shut it down**  
   ```
   docker compose-down

---

## Test Flink Job Locally
```bash
cd flink-job
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run job
python src/simple_job.py

# Run tests
pytest test/
```
---

### 🔁 CI/CD Pipeline

This repo includes a full GitLab CI/CD pipeline defined in .gitlab-ci.yml with the following stages:
| Stage         | Description                              |
| ------------- | ---------------------------------------- |
| `build_flink` | Builds Flink job from `requirements.txt` |
| `test_flink`  | Runs PyFlink unit tests                  |
| `test_nifi`   | Validates NiFi JSON template syntax      |
| `deploy_dev`  | Deploys Flink + NiFi to dev via REST API |
| `deploy_prod` | Manual trigger to deploy to production   |


###  Deployment Scripts
| Script                     | Role                                           |
| -------------------------- | ---------------------------------------------- |
| `deploy/deploy-flink.sh`   | Uploads and runs Flink job via Flink REST API  |
| `nifi-flow/deploy-nifi.sh` | Deploys NiFi flow via NiFi REST API or Toolkit |


### Configuration

Environment variables (e.g. Flink/NiFi endpoints) are defined in:
```bash
deploy/config.env
```
Or override in GitLab CI/CD settings.

## Project Structure


```text
.  
realtime-ci-flink-nifi/
├── .gitlab-ci.yml # GitLab pipeline definition
├── docker-compose.yml # Docker-based cluster setup
├── flink-job/ # PyFlink job source & tests
│ ├── src/
│ ├── test/
│ ├── requirements.txt
│ └── README.md
├── nifi-flow/ # NiFi flow templates & deploy scripts
│ ├── flow-template.json
│ ├── deploy-nifi.sh
│ └── README.md
├── deploy/ # Flink deployment logic
│ ├── deploy-flink.sh
│ └── config.env
├── docs/ # Diagrams, architecture docs
│ └── architecture.md
└── README.md 

```