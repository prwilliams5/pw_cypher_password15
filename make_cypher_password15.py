import requests
from morpheuscypher import Cypher
 
api_key = Cypher(morpheus=morpheus, ssl_verify=False).get('secret/pw_api_key:api_key')
 
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {api_key}"
    }
    
url = "https://cloudkey.corp.gipnetworks.com/api/cypher/password/15/userpass"
 
response = requests.get(url, headers=headers, verify=False)
 
print(response.text)