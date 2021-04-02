import requests, json
import subprocess
import sys

from pip._vendor.distlib.compat import raw_input

authorize_url = "https://sandbox-api.digikey.com/v1/oauth2/authorize"
token_url = "https://sandbox-api.digikey.com/v1/oauth2/token"


#callback url specified when the application was defined
callback_uri = "https://monarchele.com"

test_api_url = "https://sandbox-api.digikey.com/Search/v3/Products/p5555-nd"

#client (application) credentials - located at apim.byu.edu
client_id='6Isc2Yl1YSqHGOVGIbXE9xvk87s3KRHj'
client_secret='Ab8qfVDjF9yrHisq'


#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = raw_input('code: ')
print(authorization_code)

# step I, J - turn the authorization code into a access token, etc
#data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}

data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri, 'client_id': client_id, 'client_secret': client_secret}
print("requesting access token")
#access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False)

print(access_token_response)

print("response")
print(access_token_response.headers)
print('body: ' + access_token_response.text)


# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print("access token: "+access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token,'X-DIGIKEY-Client-Id': '6Isc2Yl1YSqHGOVGIbXE9xvk87s3KRHj'}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)
