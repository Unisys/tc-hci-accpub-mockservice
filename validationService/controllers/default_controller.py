import connexion
import six
import json
import flask
from flask import request
import requests
from validationService.conf import AUTH_URL
from validationService import util


def validate_get(Authorization=None):  # noqa: E501

    """validate_get

     # noqa: E501

    :param Authorization: an authorization header token
    :type Authorization: str

    :rtype: None
    """
    token = request.headers.get('Authorization')
    print(token)
    headers = {
        'Authorization': token
    }

    print(headers)

    print("before request")

    # response = requests.get(AUTH_URL,headers=headers,verify = false)
    response = requests.get(AUTH_URL, headers=headers, verify=False)
    print("AUTH_URL", AUTH_URL)
    print("response", response)

    if response.status_code == 200:
        response = flask.make_response()
        response.status_code = 200
        response.type = 'application/json'
        response.data = json.dumps({"Message": "Verified and authorised"})
        return response

    elif (response.status_code == 401):
        response = flask.make_response()
        response.status_code = 401
        response.type = 'application/json'
        response.data = json.dumps({"Message": "Unauthorised"})
        return response

    elif (response.status_code != 200):
        response = flask.make_response()
        response.status_code = 500
        response.type = 'application/json'
        response.data = json.dumps({"Authorisation failure"})
        return response










