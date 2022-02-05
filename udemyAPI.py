from textwrap import indent
from requests.auth import HTTPBasicAuth
#from dotenv import load_dotenv
import os 
import requests
import json

# load_dotenv()
# TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
# TWILIO_ACCOUNT_TOKEN = os.environ.get("TWILIO_ACCOUNT_TOKEN")

page_number = 1
merged_title = []
new_results = True
auth = HTTPBasicAuth("IS7xRdMNfGSmTBrXmnmelUSmN3nK7zEo1qgQ6gNt", "PBguBVWa6JjkTtcwN0Grjas2Or7Ii6nN9amvmjCSjJsh3JHGQyLkBodwfYUWTgkXdjSeP02iyOIjyEOw6tMKG3mUlybh9fyrSONhiB0ga7vWSR6HI3crq84HEYATk8jW")

while new_results:
    api_endpoint = f'https://www.udemy.com/api-2.0/courses/?page={page_number}&page_size=100'
    response = requests.get(api_endpoint , auth = auth)
    print(response.status_code)

    x = response.content
    employee_dict = json.loads(x)
    formatted_x = json.dumps(employee_dict, indent=4)
    print(type(formatted_x))
    print(type(employee_dict))
    with open(f'outputfile_{page_number}.json', 'w') as outf:
        outf.write(formatted_x)

    for title in employee_dict["results"]:
        merged_title.append(title['title'])
    page_number += 1
    if page_number == 5:
        break

#print(merged_title)
# with open('outputfile.json', 'w') as outf:
#     outf.write(formatted_x)

# for idx, item in enumerate(response.json()['calls']):
#     print(f"{idx+1}. {item['duration']}")

# print(employee_dict["results"][0]["title"])
# print(range(len(employee_dict["results"])))
