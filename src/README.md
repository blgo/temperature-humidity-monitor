# Configure your virtualenv to keep configurations isolated from other projects

```
virtualenv env
# Use the virtual environment we have created
source env/bin/activate
```

Install the package requirements.

```
pip install django

pip install djangorestframework
```
Initialise database

```
python manage.py makemigrations snippets
python manage.py migrate
python manage.py runserver
```

