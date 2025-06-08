#!/bin/bash

set -e

cd "$(dirname "$0")"

cd ..

echo "Starting Tests..."

python3 manage.py test
