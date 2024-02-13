# Data Engineering Portfolio Project
## ycmy-project
This project sets up Apache Airflow and JupyterHub on a virtual machine in Azure, with continuous integration and continuous deployment (CI/CD) through Azure DevOps.

## Project Structure

- `.env`: Environment variables necessary for configuring the services.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `airflow.cfg`: The configuration file for Apache Airflow. It's customized with `base_url` and `endpoint_url` to meet the needs of this setup.
- `docker-compose.yml`: Defines services, networks, and volumes for Docker containers.
- `Dockerfile`: Instructions for building the Docker image for the project.
- `example_dags.py`: A sample DAG file for Airflow to demonstrate the setup.
- `README.md`: Documentation to help understand and navigate the project.
- `requirements.txt`: Lists all the Python dependencies required for the project.
- `update_dags.sh`: A shell script utilized in the CI/CD pipeline to update DAGs in both Azure DevOps and the VM.
- `azure-pipelines.yml`: Defines the CI/CD pipeline for Azure DevOps.

### sites-available

- `default`: This file is for rerouting the host of Airflow and JupyterHub in the VM to the main domain of the VM.

## CI/CD Integration

The `update_dags.sh` script is part of the CI/CD process, used to synchronize DAG updates between Azure DevOps and the virtual machine. The `azure-pipelines.yml` file contains the pipeline definition for Azure DevOps, orchestrating the build and deployment processes.

## Setup and Configuration

### Airflow

The `airflow.cfg` file contains the necessary configurations for Airflow. Make sure to update the `base_url` and `endpoint_url` to point to your domain and meet your network setup.

### JupyterHub

To access JupyterHub, ensure that the `sites-available/default` file is correctly configured to route the domain to your VM's IP address.

## Usage

To start the services, ensure Docker is installed and running, then execute:

```bash`
docker-compose up -d

# Contribute
If you would like to contribute to this project, please fork the repository and submit a pull request. 
