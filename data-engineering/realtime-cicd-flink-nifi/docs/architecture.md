# CI/CD for Flink + NiFi

## Overview
This system automates the build, test, and deployment of:
- Apache Flink jobs (real-time processing)
- Apache NiFi flows (data ingestion)

## Tools
- GitLab CI/CD
- Flink REST API
- NiFi REST API
- Docker (optional for containerization)
- Prometheus + Grafana for monitoring

## Workflow
1. Commit code to GitLab
2. GitLab runs `.gitlab-ci.yml`
3. CI stages build & test jobs
4. CD stages deploy to DEV or PROD

## Monitoring
Use:
- Flink Dashboard (Prometheus JMX metrics)
- NiFi built-in monitoring + external Prometheus exporter
