#! /bin/sh

# Export needed flask environment variables
export FLASK_APP=vuln_app.py
export FLASK_ENV=development

# Change to directory ./app
cd ./app

# Flask run's - using environment variable FLASK_APP for firing the app
flask run
