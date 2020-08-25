from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    secret='baoaboaaoaaoab'
    credentials='usususususus'
    username="blblblblb"
    password="ffff"
    key='iiwiwiwiwiwi'
    return 'Hello, World!'
