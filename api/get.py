import requests

response = requests.get("http://127.0.0.1:666/user/?user=Strimis10")
response.raise_for_status()
print(response.json())