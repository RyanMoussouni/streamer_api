#Streamer API

## Initializing the databse
A database sample is available in the repository. But in case you want to initialize a new one yourself, you can follow this procedure:
- open the database using sqlite3
- create and populate the *streamers* table. 


The *streamers* table:

| username | streamingPlatform | streamingURL | profilePictureURL |
|----------|-------------------|--------------|-------------------|

## Launching the API
- install the requirements using the requirements.txt file. 
- install the twitch CLI and add it to your PATH, as it is used to request data from the twitch API
- launch the app

To launch the app:
'''python3
export FLASK_APP=src/web_app.py
flask run
'''