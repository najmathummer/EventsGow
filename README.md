In Local Environment:
Install pipenv
pipenv install
pipenv shell
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
Uncomment BASE_URL = "http://localhost:8000/" and comment the production base url
Debug =True


In Production:
BASE_URL = "https://eventsgow.pythonanywhere.com/"
Debug = False

