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

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Run API Server
python manage.py runserver
```

## Usage
```bash
# Users can be added by the administrator only
# Authentication is Basic i.e. username and password.
# For example here, username is 'usera'.
# And password is 'thisthisthis'.

# To retreive list of movies add by user
$ curl -X GET http://127.0.0.1:8000/movies/ -u usera:thisthisthis
# [{"id":2,"title":"Parasite","date":"2020-01-31"}]

# To search for a movie in all of the database
$ curl -X GET http://127.0.0.1:8000/movies/\?search\=pre -u usera:thisthisthis
# [{"id":4,"title":"Prestige","date":"2006-10-17"}]

# To add a movie
$ curl -X POST http://127.0.0.1:8000/movies/ -u usera:thisthisthis -d 'title=Maleficent&date=2014-05-30'
# {"id":5,"title":"Maleficent","date":"2014-05-30"}

# To sort the list of movies (owned by the user) by date
$ curl -X GET http://127.0.0.1:8000/movies/\?sort\=date -u usera:thisthisthis
# [{"id":6,"title":"Titanic","date":"1997-11-18"},{"id":5,"title":"Maleficent","date":"2014-05-30"},{"id":2,"title":"Parasite","date":"2020-01-31"}] 

# To sort the list of movies (owned by the user) by title
$ curl -X GET http://127.0.0.1:8000/movies/\?sort\=title -u usera:thisthisthis
# [{"id":5,"title":"Maleficent","date":"2014-05-30"},{"id":2,"title":"Parasite","date":"2020-01-31"},{"id":6,"title":"Titanic","date":"1997-11-18"}]


# To get list of users
$ curl -X GET http://127.0.0.1:8000/users/ -u usera:thisthisthis
```