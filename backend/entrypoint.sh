#!/bin/sh
set -e

# Setup db, in prod should be a proper migration system
python db.py

exec fastapi run main.py
