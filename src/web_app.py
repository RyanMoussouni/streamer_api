from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

def query_internal_db(query: str):
    return
def query_twitch_db(query: str):
    return

@app.route("/", methods=["GET"])
def main():
    return "Streamer REST API main page"

@app.route("/streamers/<streamer_name>", methods=["GET"])
def get_streamer(streamer_name: str):
    return

@app.route("/streamers/", methods=["GET"])
def get_streamers():
    return

@app.route("/streamers/", methods=["POST"])
def set_streamer():
    return

@app.route("/streamers/<streamer_name>", methods=["DELETE"])
def del_streamer():
    return