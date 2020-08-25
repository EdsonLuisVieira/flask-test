from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    secret='baoaboaaoaaoab'
    credentials='usususususus'
    user="blblblblb"
    key='iiwiwiwiwiwi'
    return 'Hello, World!'
