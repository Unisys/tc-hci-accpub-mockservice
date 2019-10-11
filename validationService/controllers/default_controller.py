import connexion
import six
from flask import request
import requests
from validationService.conf import AUTH_URL
from validationService import util


def validate_get():  # noqa: E501
    """validate_get

     # noqa: E501

    :param Authorization: an authorization header token
    :type Authorization: str

    :rtype: None
    """
    token = request.headers.get('Authorization')

    headers = {
            'Authorization': token
    }

    try:
        response = requests.get(AUTH_URL,headers=headers,verify = false)

        if(response=='dSgdSFDHGSdHJ'):

            return "success"
    except Exception as error:
        response ={
            error: "Exception occured while calling the uRL"
        }

        return response


        if isInstance(response, ErrorObject):
            return 500
        elif response.status_code == 401:
            return response
        elif response.status_code != 200:
            return 500


    

