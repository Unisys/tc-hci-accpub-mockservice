import connexion
import six
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

    headers = {
            'Authorization': token
    }

    try:
        #response = requests.get(AUTH_URL,headers=headers,verify = false)
        response = request.get(AUTH_URL,headers=headers,verify = false)



        # if response.status_code == 200:
        #     return 'success'
        # else :
        #     return 'failure'


        if(response==token):

            return "success"
        else :
            response = {
                     "error": "Exception occured while calling the uRL"
                            }
            return response
    except Exception as error:
        response ={
            "error": "Exception occured while calling the uRL"
        }

        return response




    

