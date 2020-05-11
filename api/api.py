from Flask import flask
from time import time

app = Flask(__name__)

@app.route('/time')
def get_time():
    return {"time": time.time()}
