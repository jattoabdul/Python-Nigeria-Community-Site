Install
=========

This is where you write how to get a new laptop to run this project.
- git clone

#### BACKEND SETUP
- setup virtual environment (preferable with the following names, pyngvenv|venv|env): `virtualenv pyngvenv`
- activate virtual environment `source pyngvenv/bin/activate`
- Install application local requirements `pip install -r requirements/local.txt`
- Create Database `createdb python_nigeria_site`
- Migrate DB: `python manage.py migrate`
- Create SuperUser : `python manage.py createsuperuser`
- Checkout to `develop` branch
- Run Server `python manage.py runserver`
- Explore
PS: Before making changes or raising PRs, remember to create a new branch off `develop` and raise PRs to `develop`