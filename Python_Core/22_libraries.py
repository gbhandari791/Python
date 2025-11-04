import requests

response = requests.get("https://api.github.com")
print(response)                 # Shows the response object
print(response.status_code)     # Shows HTTP status code
print(response.text)            # Shows the response content