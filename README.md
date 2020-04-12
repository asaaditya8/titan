# DRF Assignment

 ## How to run
 ```bash
git clone https://github.com/asaaditya8/titan.git
cd titan

# Create a virtual environment
python3 -m venv env
source env/bin/activate

# Install Django and DRF
pip install django
pip install djangorestframework

# Run API Server
python manage.py runserver
```

## Usage
```bash
# Users can be added by the administrator only
# Authentication is Basic i.e. username and password.

# To retreive list of movies add by user
$ curl -X GET http://127.0.0.1:8000/movies/ -u usera:thisthisthis
# [{"id":2,"title":"Parasite","date":"2020-01-31"}]

# To search for a movie in all of the database
$ curl -X GET http://127.0.0.1:8000/movies/\?search\=pre -u usera:thisthisthis
# [{"id":4,"title":"Prestige","date":"2006-10-17"}]

# To add a movie
$ curl -X POST http://127.0.0.1:8000/movies/ -u usera:thisthisthis -d 'title=Maleficent&date=2014-05-30'
# {"id":5,"title":"Maleficent","date":"2014-05-30"}

# To get list of users
$ curl -X GET http://127.0.0.1:8000/users/ -u usera:thisthisthis
```