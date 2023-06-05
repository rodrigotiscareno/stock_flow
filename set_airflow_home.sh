#!/bin/bash
cd "$(dirname "$0")"
source airflow/bin/activate
export AIRFLOW_HOME=$(pwd)


lsof -i :8080  