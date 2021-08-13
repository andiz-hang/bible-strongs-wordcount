import requests
import sys

if len(sys.argv) != 2:
    print("Error: must have at least one argument!")
    exit()

query = {'strongs': sys.argv[1]}
response = requests.get("https://api.biblesupersearch.com/api/strongs", params=query)

if response.json()['results'][0]['tvm']:
    print('TVM: ', response.json()['results'][0]['tvm'])

else:
    print('Entry: ', response.json()['results'][0]['entry'])