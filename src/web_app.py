from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

db_name = "streamers"
PATH_TO_TWITCH_BIN = "/usr/local/bin/twitch"


def query_internal_db(query: str):
    return
def query_twitch_db(query: str):
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
    query = "SELECT {} FROM {}"
    res_itrn = query_internal_db(query.format(streamer_name, db_name))
    
    if res_itrn:
        return to_json(res_itrn)
    else:
        res_twitch = query_twitch_db(query)
        
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