import requests
import base64
import mimetypes

################# API SETUP
url = 'https://prod-48.westeurope.logic.azure.com:443/workflows/eb0f0bf4e2f3412e8191ec702f8e3445/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=R_4jPOdzn9LHCJNiLNUzNzVTHpFL2NFAxpodd150nAU'

token = '57964aa2-6c3e-4710-8881-e1da54eb3938'

headers = {
    'Secret': token,
    'Content-Type': 'application/json'
}
#######################


file_path = 'գույք և երկրաշարժ 4.xlsx'

# Determine the content type
content_type, encoding = mimetypes.guess_type(file_path)
if content_type is None:
    # If content type cannot be determined, set a default or handle the case as needed
    content_type = "application/octet-stream"  # Default to binary data type

# Read the file content
with open(file_path, 'rb') as file:
    binary_data = file.read()

# Encode the binary data to base64
base64_encoded_data = base64.b64encode(binary_data).decode('utf-8')


data = {
    'title': file_path,
    'content': {
        "$content-type": content_type,
        "$content": base64_encoded_data
        },
    'email': 'rafayel.avagyan@efes.am'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to send POST request. Status code: {response.status_code}")
