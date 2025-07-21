#!/bin/bash
NIFI_HOST=$1
FLOW_JSON="nifi-flow/flow-template.json"

echo "Deploying NiFi flow to $NIFI_HOST"

# Example: uploading template (this depends on your NiFi Registry setup)
curl -X POST "$NIFI_HOST/nifi-api/process-groups/root/templates/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "template=@$FLOW_JSON"

echo "Done deploying NiFi template."
