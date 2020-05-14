from flask import Flask
from time import time

app = Flask(__name__, static_folder='build', static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_time():
    return {"time": time()}
