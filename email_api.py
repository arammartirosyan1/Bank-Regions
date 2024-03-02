import requests


url = 'https://prod-48.westeurope.logic.azure.com:443/workflows/eb0f0bf4e2f3412e8191ec702f8e3445/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=R_4jPOdzn9LHCJNiLNUzNzVTHpFL2NFAxpodd150nAU'

data = {
    'key1': 'value1',
    'key2': 'value2'
}

token = '57964aa2-6c3e-4710-8881-e1da54eb3938'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to send POST request. Status code: {response.status_code}")
