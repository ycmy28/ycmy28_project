# 💼 Interview Task Response – CI/CD Pipeline for Flink + NiFi

---

## a. How would you handle versioning of deployed Flink jobs and NiFi flows?

### Apache Flink
- Version control is handled via Git branches and tags (e.g. `v1.0.0`).
- Job artifacts (`.py`, `.jar`) are either:
  - Uploaded directly to Flink cluster via REST API during deploy phase
  - Or, optionally packaged into Docker images for Kubernetes-based deployments

### Apache NiFi
- Flows are exported as versioned JSON templates stored in `nifi-flow/` directory under Git.
- NiFi Registry can be integrated for semantic versioning and UI-based rollback.
- Deployment is done via NiFi REST API or NiFi Toolkit (`nifi.sh deploy-flow`).

---

## b. How would you test Flink jobs and NiFi flows before deploying to production?

### Apache Flink
- Python jobs use `pytest` for unit tests
- Optional: run in a local Flink mini-cluster for integration testing
- CI/CD runs `pytest` in the `test_flink` stage of GitLab

### Apache NiFi
- Flows are validated with `jq` to ensure JSON structure
- (Advanced) Use NiFi Toolkit’s `flow-verify` or dry-run to validate compatibility
- Manual testing on local/dev NiFi instance before Git commit

---

## c. How can you monitor Flink jobs and NiFi workflows once deployed?

### Apache Flink
- Flink Dashboard exposes REST metrics on port `8081`
- Integrate with **Prometheus JMX Exporter** to forward metrics
- Create Grafana dashboards for:
  - Task throughput
  - Latency
  - Job status
  - Restarts/errors

### Apache NiFi
- Native UI (http://localhost:8080/nifi) shows:
  - Backpressure
  - Flowfile queues
  - Bulletins (errors/warnings)
- Prometheus reporting task available (NiFi 1.10+)
- Alerts via external systems like PagerDuty or email

---

## d. What changes would you make if running Flink and NiFi on Kubernetes?

### Apache Flink
- Use **Flink Kubernetes Operator** to manage job lifecycle as Kubernetes CRDs
- Create Helm chart or Kustomize manifests for `JobManager`, `TaskManager`
- Mount secrets/configs via `ConfigMap` or `Secret`
- Autoscaling with HPA based on job load

### Apache NiFi
- Run as **StatefulSet** with persistent volume for flow state
- Use NiFi Helm chart for easier deployment
- Externalize NiFi config via `ConfigMap`
- Use NiFi Registry for flow lifecycle mgmt
- Secure with Ingress + TLS + OIDC or LDAP

---

## 📦 Additional Notes

- Project includes full GitLab CI/CD config (`.gitlab-ci.yml`)
- Scripts:
  - `deploy/deploy-flink.sh` — REST-based Flink job deployment
  - `nifi-flow/deploy-nifi.sh` — REST upload of NiFi flow
- Deployed locally via Docker Compose (for demo) but designed for cloud-native upgrade

---

## 🧪 Sample Commands to Simulate Deployment

```bash
docker compose up -d                        # Boot local Flink + NiFi
pytest flink-job/test/                     # Run Flink unit tests
./deploy/deploy-flink.sh http://localhost:8081
./nifi-flow/deploy-nifi.sh http://localhost:8080
