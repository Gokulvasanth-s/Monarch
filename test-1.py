import requests

url = "https://api.mouser.com/api/v1/search/keyword?apiKey=bfad76ba-7837-4d46-86d0-036fe7cd00c7"

payload="{\n  \"SearchByKeywordRequest\": {\n    \"keyword\": \"CC0402KRX5R6BB105\",\n    \"records\": 0,\n    \"startingRecord\": 0,\n    \"searchOptions\": \"string\",\n    \"searchWithYourSignUpLanguage\": \"string\"\n  }\n}"
headers = {
  'Content-Type': 'application/json',
  'version': '1',
  'Cookie': 'ASP.NET_SessionId=wu2c4jlto2fnl0fqhykikbdn'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)