from mongo_doc import init_db, create_collection_class
from mqtt_client import connect_client
import time
import json


def main2():
    init_db('mongodb://localhost:27017', 'IoT')

    Value = create_collection_class('Value', 'temperatures')

    for value in Value.all_iter():
        print('date:', value['date'])
        print('time:', value['time'])
        print('temperature:', value['temperature'])
        print()
        time.sleep(10)

def main():
    client = connect_client('pub1')
    init_db('mongodb://localhost:27017', 'IoT')

    Value = create_collection_class('Value', 'temperatures')

    for value in Value.all_iter():
        value = json.dumps(value)
        client.publish('iths/temperature/temp1', payload=value, qos=0)
        print("Published:", value)
        time.sleep(10)


if __name__ == '__main__':
    main()
