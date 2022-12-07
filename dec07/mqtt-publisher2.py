from mongo_doc import init_db, create_collection_class
from mqtt_client import connect_client
import time
import json


def main():
    client = connect_client('pub2')
    init_db('mongodb://localhost:27017', 'IoT')

    Value = create_collection_class('Value', 'temperatures')

    for value in Value.all_iter():
        value = json.dumps(value)
        client.publish('iths/hepp/temp2', payload=value, qos=0)
        print("Published:", value)
        time.sleep(5)


if __name__ == '__main__':
    main()
