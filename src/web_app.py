import os
import json

from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

db_name = "streamers"
PATH_TO_TWITCH_BIN = "/usr/local/bin/twitch"
PATH_TO_DATABASE = "streamers.db"


def query_internal_db(query: str):
    return
def query_twitch_db(streamer_name: str):
    command = "twitch api get users -q login={}".format(streamer_name)
    response = json.loads(os.popen(command).read())

    res = response["data"]
    
    return


def to_json(query_result):
    return
def update_internal_db(query_result):
    return

@app.route("/", methods=["GET"])
def main():
    return "Streamer REST API main page"

@app.route("/streamers/<streamer_name>", methods=["GET"])
def get_streamer(streamer_name: str):
    query = "SELECT * FROM {} WHERE username=?".format(db_name)
    res_itrn = query_internal_db(query)
    
    if res_itrn:
        return to_json(res_itrn)
    else:
        res_twitch = query_twitch_db(streamer_name)
        
        if res_twitch:
            update_internal_db(res_twitch)
            return to_json(res_twitch)
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