# Metrikgile API

## [Home](https://github.com/Metrikgile/metrikgile-api/wiki)
## [Issue workflow](https://github.com/Metrikgile/metrikgile-api/wiki/Issue-Workflow)

## Requiremets
- [Python3](https://wiki.python.org/moin/BeginnersGuide/Download)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Pipenv](http://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [Docker](https://docs.docker.com/install/)

## Setting Up
1. Install project dependencies by running:
```bash
pipenv install --dev
```
2. Run a postgres container for the application database:
```bash
docker run --name db-metrikgile -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres
```
3. Access the virtual environment:
```bash
pipenv shell
```
4. Already inside the virtual environment make the migrations:
```bash
./manage.py makemigrations
```
5. Migrate the database:
```bash
./manage.py migrate
```

## Running the application
After complete the **Setting Up** steps, run the application with:
```bash
./manage.py runserver
```
