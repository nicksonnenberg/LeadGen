import requests
import base64
import json

# OAuth 2.0 for Yahoo
# Authorization process according to:
# https://developer.yahoo.com/oauth2/guide/
class OAuth(object):
    def __init__(self, key, secret, refresh_token = None):
        self.key = key
        self.secret = secret
        self.refresh_token = refresh_token
        self.base_url = 'https://api.login.yahoo.com/oauth2/'
        self.request_auth_url = self.base_url + 'request_auth'
        self.get_token_url = self.base_url + 'get_token'

        key_secret = self.key + ':' + self.secret
        self.b64authorization = base64.b64encode(key_secret.encode(encoding='UTF-8')).decode()

        if not self.refresh_token:
            code = self.get_auth_token()
            self.exchange_auth_token(code)


    def get_auth_token(self):
        data = {
            'client_id' : self.key,
            'redirect_uri': 'oob',
            'response_type': 'code',
        }
        response = requests.post(self.request_auth_url, data)
        print('Please authorise: ' + response.url)
        code = input('Code: ')
        return code

    def exchange_auth_token(self, code):
        data = {
            'client_id': self.key,
            'client_secret': self.secret,
            'redirect_uri': 'oob',
            'code': code,
            'grant_type': 'authorization_code'
        }

        headers = {
               'Authorization': 'Basic {}'.format(self.b64authorization),
               'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.get_token_url, data, headers=headers)
        json_response = json.loads(response._content.decode())
        self.refresh_token = json_response['refresh_token']
        self.access_token = json_response['access_token']
        return json_response['access_token']

    def exchange_refresh_token(self):
        data = {
            'client_id': self.key,
            'client_secret': self.secret,
            'redirect_uri': 'oob',
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }
        headers = {
               'Authorization': 'Basic {}'.format(self.b64authorization),
               'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.get_token_url, data, headers=headers)
        json_response = json.loads(response._content.decode())
        self.access_token = json_response['access_token']
        return json_response['access_token']
