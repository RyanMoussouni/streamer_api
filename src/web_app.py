import os
import json
from sqlite3.dbapi2 import Error

from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

db_name = "streamers"
PATH_TO_DATABASE = "streamers.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def query_internal_db(streamer_name: str):
    with create_connection(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  {} WHERE username=?", (streamer_name,))

        rows = cur.fetchall()
        
        if len(rows) == 0:
            res = {}
        elif len(rows) == 1:
            res = {}
            username, streamingPlatform, streamingURL, profilePictureURL = rows[0]
            res["username"] = username
            res["streamingPlatform"] = streamingPlatform
            res["streamingURL"] = streamingURL
            res["profilePictureURL"] = profilePictureURL
        else:
            raise Exception("Dupplicate data in the database")
    return res
def query_twitch_db(streamer_name: str):
    command = "twitch api get users -q login={}".format(streamer_name)
    response = json.loads(os.popen(command).read())

    try:
        res = {}
        res["steamingPlatform"] = "twitch"
        res["username"] = response["data"][0]["display_name"]
        res["profilePictureURL"] = response["data"][0]["profile_image_url"]
        res["streamingURL"] = "twitch.tv/{}".format(streamer_name)
    except IndexError:
        #no data on the streamer
        res = {}
    return res


def update_internal_db(query_result):
    with create_connection(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        streamer = query_result["userName"], query_result["streamingPlatform"], query_result["streamingURL"], query_result["profilePictureURL"]
        sql = '''UPDATE streamers
                 SET username = ?
                     streamingPlatform = ?
                     streamingURL = ?
                     profilePictureURL = ?'''
        cur.execute(sql, streamer)
        conn.commit()
    return

@app.route("/", methods=["GET"])
def main():
    return "Streamer REST API main page"

@app.route("/streamers/<streamer_name>", methods=["GET"])
def get_streamer(streamer_name: str):
    res_itrn = query_internal_db(streamer_name)
    
    if res_itrn:
        return res_itrn
    else:
        res_twitch = query_twitch_db(streamer_name)
        
        if res_twitch != {}:
            update_internal_db(res_twitch)
            return res_twitch
        else:
            return {}

@app.route("/streamers/", methods=["GET"])
def get_streamers():
    return

@app.route("/streamers/", methods=["POST"])
def set_streamer():
    return

@app.route("/streamers/<streamer_name>", methods=["DELETE"])
def del_streamer():
    return