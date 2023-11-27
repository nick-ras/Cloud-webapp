#!/bin/sh

# Source environment variables
source .env
source env/bin/activate
export APP_SETTINGS=config.DevelopmentConfig

# Run your Flask application
python3 manage.py run
