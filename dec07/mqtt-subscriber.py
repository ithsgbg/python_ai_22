from mqtt_client import connect_client
import json


def on_message(client, userdata, msg):
    topic = msg.topic
    qos = msg.qos
    message = msg.payload.decode('utf-8')
    message_dict = json.loads(message)
    print(f'Got a message on topic {topic}')
    print('Date:', message_dict['date'])
    print('Time:', message_dict['time'])
    print('Temperature:', message_dict['temperature'])
    print()


def main():
    client = connect_client("sub1")
    client.subscribe("iths/#")
    client.on_message = on_message
    client.loop_forever()



if __name__ == '__main__':
    main()
