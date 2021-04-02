import os
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

os.environ['DIGIKEY_CLIENT_ID'] = 'AydtcTOo0tgZ0v7usYt0PstlPZQQVNjH'
os.environ['DIGIKEY_CLIENT_SECRET'] = 'D8uzqMc26bA0mrvR'
os.environ['DIGIKEY_CALLBACK'] = 'https://monarchele.com'
os.environ['DIGIKEY_CLIENT_SANDBOX'] = 'False'
os.environ['DIGIKEY_STORAGE_PATH'] = '/Users/gshanmu2/Documents/python/Mouser'


# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)

# Search for parts
search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
result = digikey.keyword_search(body=search_request)
print(search_request)
print(result.products)