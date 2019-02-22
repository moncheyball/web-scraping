import requests
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/browse', methods=["GET"])
def browse():
    url = request.args.get('url', '')
    html = requests.get(url).text
    return render_template("index.html", value=url, scraping=html)
