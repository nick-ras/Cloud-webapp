This is a flask webapp, that has a db with 2 tables, a users table and a boxes table. 
I made a frontend website where users can log in and book boxes for 6-48 hours. 
A use-case could be for for box storage around a city, where users can book boxes or pick up packages or other stuff. 
I use sqlalchemy for securing against sql injection, and FLASK_WTF for CRSF.
I use JQuery for dynamic webpages.
I also my unit and integration tests in the pytests folder.
I made a docker file that succesfully creates a docker image that can be used on other ubuntu versions, since it fetches  msodbcsql18 drivers for the specific ubuntu version. For this to work your DB server would have to use microsoft sql server odbc driver, otherwise you would have to install other database drivers.
There is a couple of env vars you would have to set like APP_SETTINGS, DATABASE_URL and SECRET_KEY in order for it to work. 

I use virtual environment so you can just install the requierements.txt file in a new environment.
I have a simple setup where i just execute python with "python3 app.py run", but check in y_commands file


Tests have been implmented in pytests folder, check in y_commands file for commands