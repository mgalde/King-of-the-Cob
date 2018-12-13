# King of the Cob
Agile development doesn't need to be hard, its just needs to be done right!

Introducing King of the Cob! an AGILE / SCRUM method used for project management, scheduling, tracking and reporting without the need for expensive team management software, run everything from a Raspberry Pi on your network.

Try it out at http://live.kingofthecob.com/

![King of the Cob](/docs/images/KotC.png "King of the Cob")


When it comes to AGILE management some teams may view this as the best possible style or as a hindrance to production. Being able to track work utilizing the AGILE process is a great way to improve the teams efficiency. The problem noticed however is AGILE / SCRUM may be hard to implement if no one has done it before. Some have never even heard of a Kanban board or knows what a sprint is. This project will take the place of the SCRUM-Master for your project and will keep you and your team on track and in good communication. You will find your products will flow more efficiently with correct planning, retrospectives and development support. So why nominate a dedicated SCRUM-master when King-of-the-Cob can do it to!

## Project Requirements
* [User Stories](/docs/User_Stories.md)
* [Mis-User Stories](/docs/Mis_User_Stories.md)
* [Diagrams](/docs/diagrams.md)

## Installation
### Hardware Recommendations
* Raspberry Pi 3
* 64GB SD card
* Keyboard / Mouse / Monitor for setup

### Software Requirements
* Latest Raspbian image
* Python
* Django
* Crispy Forms
```bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install python -y
sudo pip install Django
pip install --upgrade django-crispy-forms
pip install djangorestframework
pip install markdown
pip install django-filter
```
* Download this repo
```bash
sudo apt-get update && sudo apt-get upgrade -y
git clone https://github.com/mgalde/King-of-the-Cob.git
cd King-of-the-Cob
cd Docs
cd KingoftheCobApp
```
* Start the King-of-the-Cob web service
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
You should then see something like the following:

Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.



## Getting Started & Deployment
Test it out locally by running the server from the KingoftheCobApp directory
```bash
python manage.py runserver
```

The application is Elastic Beanstalk ready, you just need to make a few minor changes.

Within settings.py change the following:
```bash
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<insert your own secret key here when you deploy KingoftheCob>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
```

```bash
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'make anything up in here that would be known only to your orginization'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['AWS internal link', 'your external link, subdomain or what have you']
```

Additionally also change
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'kotc',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

To:
```bash

if 'internal database name here' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'kotc',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

```

Finally change
```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
AUTH_USER_MODEL = 'accounts.User'           # This is important to use my own user permission models
LOGIN_REDIRECT_URL = 'connected'            # Once a user connects they go to the connected URL
LOGOUT_REDIRECT_URL = 'home'                # Everyone goes home once loged out
CRISPY_TEMPLATE_PACK = 'bootstrap4'         # Looks nicer in this template, can be changed if you wish

```

To:
```bash

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
AUTH_USER_MODEL = 'accounts.User'           # This is important to use my own user permission models
LOGIN_REDIRECT_URL = 'connected'            # Once a user connects they go to the connected URL
LOGOUT_REDIRECT_URL = 'home'                # Everyone goes home once loged out
CRISPY_TEMPLATE_PACK = 'bootstrap4'         # Looks nicer in this template, can be changed if you wish

```

Generate a new text document at the header of the project titled requirements.txt

```text
bleach==3.0.2
Django==2.1.1
django-bleach==0.3.0
django-crispy-forms==1.7.2
django-filter==2.0.0
djangorestframework==3.9.0
Markdown==3.0.1
pytz==2018.7
six==1.11.0
webencodings==0.5.1
```

Finally go within the project and change all hardcoded links to adjust for the new web address


# Code of Conduct for King of the Cob Community
* [Code of Conduct](/docs/CODE_OF_CONDUCT.md)

# License
MIT License

Copyright (c) 2018 Michael Galde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
