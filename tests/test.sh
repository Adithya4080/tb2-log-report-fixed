#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

# Run pytest and emit CTRF JSON to the verifier log directory
pytest /tests/test_outputs.py -rA \
  --json-ctrf /logs/verifier/ctrf.json

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
