# King of the Cob
Agile development doesn't need to be hard, its just needs to be done right!

Introducing King of the Cob! an AGILE / SCRUM method used for project management, scheduling, tracking and reporting without the need for expensive team management software, run everything from a Raspberry Pi on your network.

Try it out at https://kingofthecob.com

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



## Getting Started
Run the server from the KingoftheCobApp
```bash
python manage.py runserver
```

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
