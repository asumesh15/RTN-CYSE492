from taxii2client.v20 import Server, Collection
import json
from cabby import create_client
client = create_client('localhost',discovery_path='/services/discovery-a',port=9000)
client.set_auth(username='test', password='test')
#taxiiCollection = Collection('http://localhost:9000/services/collection-management-a', user='test', password='test')

server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
api_root = server.api_roots[0]
collections_limo = [api_root.collections[0]]#Phish Tank collection
for collection in collections_limo:
    print(collection.title)
    obj = collection.get_objects(limit=1)
    objStr = json.dumps(obj)
    print(objStr)
    #client.push(objStr, 'urn:stix.mitre.org:json:2.1',uri='/services/inbox-a',collection_names=['collection-a'])
    #print(obj)
    
    with open('data.json', 'w') as outfile:
        json.dump(obj, outfile)
