#!/bin/bash
cd insert_path_here
echo "Pulling latest DAGs from Azure DevOps..."
if git pull origin main; then
    echo "DAGs updated successfully."
    # Uncomment the next line if you need to restart Airflow
    # airflow restart
else
    echo "Failed to update DAGs. Check for errors!"
fi