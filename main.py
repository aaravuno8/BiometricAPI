from flask import *
import json
import time

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    dataset = {"Page": "Home"}
    json_dump = json.dumps(dataset)
    return json_dump
