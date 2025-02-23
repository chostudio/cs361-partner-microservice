import requests

url = "http://127.0.0.1:5000/ask"
headers = {"Content-Type": "application/json"}
data = {"question": "Explain the importance of blockchain"}

response = requests.post(url, json=data, headers=headers)

print(response.json())  # Print the response from the API

# how to run in terminal: python test_request.py