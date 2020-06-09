# API

## Prerequisites

```bash
Python 3.8
pip
virtualenv
```

## Run Development Server

```bash
virtualenv py_venv
source py_venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0:8000
```