import requests
from morpheuscypher import Cypher

# sets variable for api key
api_key = Cypher(morpheus=morpheus, ssl_verify=False).get('secret/pw_api_key:api_key')

# api call to create cypher password with 15 chars
url = "https://cloudkey.corp.gipnetworks.com/api/cypher/password/15/userpass"

# make sure to use an f string to use api key variable
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {api_key}"
    }
    
# use verify=False argument to ignore ssl check
response = requests.get(url, headers=headers, verify=False)
 
print(response.text)