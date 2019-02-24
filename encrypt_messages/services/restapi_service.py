import os
import requests
import json

from .service_interface import ServiceInterface

class RestAPIService(ServiceInterface):
    def __init__(self):
        self.endpoint = os.getenv("RESTAPI_ENDPOINT")
        #TODO: AUTH CONFIGURATION
    
    def post(self, cyphered_message):
        r = requests.post(self.endpoint, json={ 'content': cyphered_message })
    
    def read(self):
        resp = requests.get(self.endpoint, params={'last_item': 'true'})
        data = resp.json()
        return data['data'][0]['content']
