#!/bin/bash

cd /usr/src/app/app && uvicorn main:app --reload --port=8000 --host=0.0.0.0
# cd /usr/src/app/app && gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --log-level info main:app
