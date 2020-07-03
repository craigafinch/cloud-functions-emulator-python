"""This framework mimics the Flask framework provided by Google Cloud Functions"""
from flask import Flask
from flask import request

from example import my_function

app = Flask(__name__)


# Add your routes here
@app.route('/')
@app.route('/route1')
def caller():
    response = my_function(request)
    return response
