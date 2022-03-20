In Local Environment:
Install pipenv
pipenv install
pipenv shell
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
Uncomment BASE_URL = "http://localhost:8000/" and comment the production base url
Debug =True

for testing purposes clean_email in DefaultAccountAdapterCustom of accounts app can be edited, to allow all emails.


In Production:
BASE_URL = "https://eventsgow.pythonanywhere.com/"
Debug = False

