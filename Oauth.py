import requests
import json
import oauth2





# 1. Get Auth Code

url = "https://sandbox-api.digikey.com/v1/oauth2/authorize?response_type=code&client_id=6Isc2Yl1YSqHGOVGIbXE9xvk87s3KRHj&redirect_uri=https%3A%2F%2Fmonarchele.com%2F"



r = requests.get(url, auth=('gokulsmith@gmail.com','zxcvbnM123#'),)

h = r.headers
#rint(r.cookies)
print(r.content)

print(h)






#2. Get Access Token and Refresh Token

#3. Make an Api Call