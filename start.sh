#!/bin/bash
set -e
echo "Starting IoT Smart Home Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9073 --workers 1
