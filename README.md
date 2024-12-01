## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push

# update pipfile
pipenv update

# run venv 
pipenv shell

# run cmd inside venv
pipenv run [cmd]

# migrations may need to be applied with
python manage.py migrate
```

CSV Ingestion Layer

    - Accepts CSV uploads via a web UI or API endpoint.
    - validates the data
    - Stores the file in a staging area (s3 for bronze)
    - cleans the data (stored in db & silver s3)


FLOW:
csv input => raw landing bucket => staging bucket => 'clean' bucket  => database