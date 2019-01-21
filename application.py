from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now(timezone('America/New_York'))
    return render_template("index.html", now=now)
