import requests

cs_url = 'https://api.github.com'

r = requests.get('http://a7777777ap5l0e.com')

if r.status_code == 200:
    print(r.status_code)
