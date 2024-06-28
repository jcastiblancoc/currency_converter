# currency_converter

Steps to configure this project

Previous steps
- Install python and pip

Steps
- Create virtual environment in the root of the project python -m venv ./venv

- Add important paths to $PYTHONPATH (advise: add it in ./venv/bin/activate) HOMEPATH is the route of your root project example c:\User\project export PYTHONPATH="$HOME_PATH/packages/python:$HOME_PATH/db/python:$HOME_PATH/shared/python:$HOME_PATH"

- Install dependencies in your venv pip install -t packages/python -r requirements.txt

- Set environment variables in a .env file

- run the app: go in to /src folder in the terminal and run python app.py