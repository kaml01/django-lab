#!/bin/bash
set -e

echo "Stopping Django server..."

pkill -f "manage.py runserver" || true
