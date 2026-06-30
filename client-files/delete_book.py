import http.client

conn = http.client.HTTPConnection("127.0.0.1", 5000)
payload = ''
headers = {}
conn.request("DELETE", "/libros/300", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))