from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

client_id = '6Isc2Yl1YSqHGOVGIbXE9xvk87s3KRHj'
client_secret = 'Ab8qfVDjF9yrHisq'
redirect_uri = 'https://monarchele.com'

oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url='https://sandbox-api.digikey.com/v1/oauth2/token',username='gokulsmith@gmail.com', password='zxcvbnM123#', client_id='6Isc2Yl1YSqHGOVGIbXE9xvk87s3KRHj',client_secret='Ab8qfVDjF9yrHisq')

print(token)

