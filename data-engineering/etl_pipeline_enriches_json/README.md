# ETL Pipeline: Geocode JSON with LocationIQ & Airflow

A lightweight ETL that reads raw JSON, enriches each record with latitude/longitude via LocationIQ (free version to test), and writes out an enriched JSON—fully orchestrated by Apache Airflow and Docker Compose.

---

## 🚀 Background

In modern ETL you often need to augment datasets with third‑party geocoding. This project demonstrates a production‑grade pattern:

1. **Extract** – read `input_sample.json`  
2. **Transform** – call LocationIQ API with retries/backoff and schema checks 
3. **Load** – dump enriched JSON  
4. **Orchestrate** – Airflow DAG with collapsible ETL task group  
5. **Test** – unit tests via `pytest` in a container

---

## ✨ Features

- **Robust Geocoding** using LocationIQ free tier (sign up and put the key in Airflow variable)
- **Retries & Exponential Backoff** (via `tenacity`) on API failures  
- **Schema Validation & Structured Logging** for empty or malformed payloads  
- **Airflow DAG** with  `TaskGroup` for extract→transform→load  
- **Comprehensive Unit Tests** (`pytest`) run in their own Docker service  
- **Container‑native**: Airflow, Postgres, Redis, and test runner all defined in `docker-compose.yml`  

---

## 📦 Prerequisites

- **Docker** >= 28 
- **Docker Compose** >= v2.25.0 

---

## 🔧 Quickstart

1. **Clone**  
   ```bash
   git clone https://github.com/ycmy28/ycmy28_project.git

2. **Bring up Airflow infra**  
   ```initialize DB & create admin user
    docker compose up airflow-init

    ```initialize DB & create admin user
    docker compose up -d

3. **Configure Airflow Variable**  
   ```In the Airflow UI (http://localhost:8080 → Admin → Variables), add:
    Key:   LOCATIONIQ_KEY
    Value: pk.your_actual_key_here

4. **Running Unit Tests**  
   ```# optional: start Postgres & Redis, if not already running
    docker compose up -d postgres redis

    ```# run tests in a temporary container
    docker compose run --rm pytest

Cleanup:
docker compose down --volumes --rmi all

## Project Structure
etl_pipeline_enriches_json/
├── dags/
│   └── geocode_pipeline.py       # Airflow DAG
├── data/
│   ├── int_test_input/
│   │   └── input_sample.json     # sample raw data
│   └── int_test_output/          # enriched output
├── src/
│   ├── integrations/
│   │   ├── __init__.py
│   │   └── geocode_util.py       # geocoding utils
│   ├── transformers/
│   │   ├── __init__.py
│   │   └── address_transformer.py# enrich logic
│   └── utils/
│       ├── __init__.py
│       ├── reader.py             # JSON reader
│       └── writer.py             
├── tests/
│   ├── __init__.py
│   ├── test_geocode.py
│   ├── test_reader.py
│   ├── test_writer.py
│   └── test_transformer.py
├── requirements.txt              # runtime dependencies
├── requirements-dev.txt          # pytest, tenacity, etc.
├── setup.py                      # for `pip install -e .`
└── docker-compose.yml            # service definitions


## License

This project is open-sourced under the [MIT License](LICENSE).

---

Proudly maintained by Yudha, driven by data and inspired by possibilities.
