# Preparation

```python
python3 -m venv asicsapi
cd asicsapi/
source bin/activate
git init
touch .gitignore
pip3 install -r requirements.txt

pip install fastapi
pip install uvicorn[standard]
pip install databases[sqlite]
pip install python-multipart

# pip install 'fastapi-users[sqlalchemy]'
```

## Create main.py

## Run
```
uvicorn  main:app --reload
```

## Overview of Program Logic
1. Main.py comtains the routes
2. Data_models contains classes for requests aand responses defined using Pydantic. Validations on data are also defined here.
3. A Data_model class gets instantiated inside a function defined under a route. We automatically get validation errors 


## Resources
 - https://betterprogramming.pub/the-beginners-guide-to-pydantic-ba33b26cde89
