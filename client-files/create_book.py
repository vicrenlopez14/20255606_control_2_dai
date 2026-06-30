import requests

url = "http://127.0.0.1:5000/libros"

payload = "{\n    \"id\": 300,\n    \"titulo\": \"Nuevo libro\",\n    \"autor\": \"Chespiro\",\n    \"disponible\": true\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


