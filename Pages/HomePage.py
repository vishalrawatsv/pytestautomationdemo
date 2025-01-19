#homepage changes
import json

p = json.dumps({'name': 'vishal'})
print(p)
endpoint = '/api/node/class/{object_type}.json'.format(object_type="vishal")
object_type="rawat"
endpoint2 = f"/api/node/class/{object_type}.json"
print(endpoint)
print(endpoint2)
