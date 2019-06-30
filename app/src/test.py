import requests



response = requests.get('localhost:5000')
status_code = response.status_code
print(response.text)