"""This code gets deployed to Google Cloud Functions"""

import os
import json
from flask import Response


def my_function(request):
    """Returns a Flask Response object

    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    # This is how you access an environment variable (whether running locally or on GCP)
    os.environ.get('MY_VAR')

    # This is an example of returning a JSON payload
    payload = {
        "full_path": request.full_path,
        "args": request.args
    }
    flask_response = Response(response=json.dumps(payload), status=200)
    flask_response.headers['Content-Type'] = 'application/json;charset=utf-8'

    return flask_response
