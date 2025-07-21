#!/bin/bash
# Replace these with your environment values
NIFI_API="http://nifi-host:8080/nifi-api"
REGISTRY_ID="your-registry-id"
FLOW_ID="your-flow-id"

curl -X POST "$NIFI_API/versions/flows/$FLOW_ID" \
     -H "Content-Type: application/json" \
     -d '{
           "version": 2,
           "clientId": "ci-cd-pipeline",
           "registryId": "'$REGISTRY_ID'",
           ...
         }'
