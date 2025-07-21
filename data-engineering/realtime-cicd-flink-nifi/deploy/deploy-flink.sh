#!/bin/bash
FLINK_API=$1
JAR_PATH=$(find flink-job/target/ -name "*.jar" | head -n 1)

echo "Uploading JAR to Flink..."
JAR_ID=$(curl -s -X POST -H "Expect:" -F "jarfile=@$JAR_PATH" "$FLINK_API/jars/upload" | jq -r '.filename' | awk -F'/' '{print $NF}')

echo "Running Flink job..."
curl -X POST "$FLINK_API/jars/$JAR_ID/run" \
  -H "Content-Type: application/json" \
  -d '{}'
