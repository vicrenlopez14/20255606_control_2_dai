import http.client

conn = http.client.HTTPConnection("127.0.0.1", 5000)
payload = "{\n    \"id\": 300,\n    \"titulo\": \"Nuevo libro ya no es nuevo\",\n    \"autor\": \"Chespiro 2\",\n    \"disponible\": false\n}"
headers = {}
conn.request("PUT", "/libros", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))