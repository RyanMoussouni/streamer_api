from flask import Flask
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def main():
    return "Streamer REST API main page"