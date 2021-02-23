from taxii2client.v20 import Server, Collection
import json
server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
api_root = server.api_roots[0]
collections_limo = [api_root.collections[0]]#Phish Tank collection
for collection in collections_limo:
    print(collection.title)
    obj = collection.get_objects(limit=1)
    print(obj)
    #with open('data.json', 'w') as outfile:
    #    json.dump(obj, outfile)