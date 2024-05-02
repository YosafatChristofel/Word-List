import requests

api_key = 'https://dictionaryapi.com/account/example?key=d181b5f6-bfa4-4954-b781-0f1c144116db'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)