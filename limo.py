from taxii2client.v20 import Server, Collection, as_pages
import json
from cabby import create_client
from datetime import datetime
from pytz import timezone
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--collection", help="Enter a collection number (0, 1, 2..)")
args = parser.parse_args()

tz = timezone('US/Eastern')
#client = create_client('localhost',discovery_path='/services/discovery-a',port=9000)
#client.set_auth(username='test', password='test')
#taxiiCollection = Collection('http://localhost:9000/services/collection-management-a', user='test', password='test')
collectionNum = int(args.collection)
server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
api_root = server.api_roots[0]
collections_limo = [api_root.collections[collectionNum]]#collection name
for collection in collections_limo:
    print(collection.title)
    obj = collection.get_objects()

    objects = obj['objects']
    for item in objects:
        if 'description' in item:
            description = item['description']
            ##label = item['labels'][0].replace('-', ' ') 
            #threatstream_severity = item['labels'][1].split("threatstream-severity-")[1]
            #threatstream_confidence = float(item['labels'][2].split("threatstream-confidence-")[1])
            #item['label'] = label
            #item['threatstream_severity'] = threatstream_severity.replace('-', ' ') 
            #item['threatstream_confidence'] = threatstream_confidence
            item['collection'] = collection.title
            item['dataSource'] = "Anomali Limo"
            #item['iType'] = description.split(";")[1].split(":")[1].lstrip()
            #item['state'] = description.split(";")[2].split(":")[1].lstrip()
            #item['name'] = item['pattern'].split("'",1)[1][:-2]
            #item['marking_definition'] = item['object_marking_refs'][0].split("--")[1]
            item['ingestDate'] = datetime.now(tz).isoformat()
            item['isValidStix'] = "Yes"
            #print(re.search("(?P<url>https?://[^\s]+)", item["name"]).group("url"))
            #ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', item["name"]).group()
            del item['labels']
            #del item['pattern']
            del item['object_marking_refs']
    objStr = json.dumps(obj)
    #client.push(objStr, 'urn:stix.mitre.org:json:2.1',uri='/services/inbox-a',collection_names=['collection-a'])
    #print(obj)
    fName = collection.title + ".json"
    fName.replace(" ", "-")
    #with open(fName, 'w') as outfile:
    #    json.dump(obj, outfile)
