::Executable
::Launches the python script to run the website, website will then automatically launch to the homepage
@echo off
::run python script
start python manage.py runserver
::create a pause so the application can fully load
timeout /t 3 /nobreak
::launch the webpage using the local host and appropiate application page
start http://localhost:8000/Power/DNP3/DNP3/