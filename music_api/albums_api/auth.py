# followed this YouTube video to build this file: https://youtu.be/xdq6Gz33khQ

from http import client
from lib2to3.pgen2 import token
import requests
import base64
import datetime

client_id = 'a99dfe235c814dcda823e58b44a28596'
client_secret = '55495c730dda4c95991bca5dcd6a8247'

# do a lookup for a token
# this token is for future requests
# tokens do expire
# you authenticate one time, then can access same session until token expires without re-logging in

# https://developer.spotify.com/documentation/general/guides/authorization/
# choose client credentials authorization flow

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()) # more secure way to pass credentials, turns into base64 encoded bytes rather than string

# client_creds.encode() # turns client_creds from str into bytes
# base64.b64decode(client_creds_b64) would decode b64 str back into a byte str with original client_creds value -- this comment just here for reference. We aren't using this here. Spotify backend probably uses a line like this though

token_url = 'https://accounts.spotify.com/api/token'
method = "POST"
token_data = {
  "grant_type": "client_credentials",
}

token_headers = {
  "Authorization": f"Basic {client_creds_b64.decode()}", # <base64 encoded client_id:client_secret> base64 encoded str
}

# in theory, using python requests module/package means we don't have to worry about urlencoding
r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json()) # should display full access token object
valid_request = r.status_code in range(200, 299) # gives Boolean for valid request

if valid_request: 
  token_response_data = r.json()
  now = datetime.datetime.now()
  access_token = token_response_data['access_token']
  expires_in = token_response_data['expires_in'] # seconds
  expires = now + datetime.timedelta(seconds=expires_in)
  did_expire = expires < now

