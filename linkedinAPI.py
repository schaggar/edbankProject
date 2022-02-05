from textwrap import indent
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from decouple import config
import os 
import requests
import json

load_dotenv()
LINKEDIN_ACCOUNT_SID = config('LINKEDIN_ACCOUNT_SID')
LINKEDIN_ACCOUNT_TOKEN = config('LINKEDIN_ACCOUNT_TOKEN')


auth = HTTPBasicAuth(LINKEDIN_ACCOUNT_SID, LINKEDIN_ACCOUNT_TOKEN)

api_endpoint = 'https://www.linkedin.com/oauth/v2/authorization'
response = requests.get(api_endpoint , auth = auth)
print(response.status_code)

#print(merged_title)
# with open('outputfile.json', 'w') as outf:
#     outf.write(formatted_x)

# for idx, item in enumerate(response.json()['calls']):
#     print(f"{idx+1}. {item['duration']}")

# print(employee_dict["results"][0]["title"])
# print(range(len(employee_dict["results"])))
