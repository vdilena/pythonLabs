import http.client

host = 'es.jooble.org'
key = '79246bea-67e3-41f9-8869-58ef5be20d24'

connection = http.client.HTTPConnection(host)
#request headers
headers = {"Content-type": "application/json"}
#json query
body = '{ "keywords": "Desarrollador", "location": "Argentina"}'
connection.request('POST','/api/' + key, body, headers)
response = connection.getresponse()
print(response.status, response.reason)
print(response.read())