import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f'CONNACK recieved with code {rc}')


def connect_client(client_id):
    client = paho.Client(client_id=client_id, userdata=None, protocol=paho.MQTTv5)

    client.on_connect = on_connect
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("ithsuser", "s3cr37s3cr37")
    client.connect("3b18baa54b4e4dc391287799af1136d0.s1.eu.hivemq.cloud", 8883)
    # client.username_pw_set("user", "password")
    # client.connect("localhost", 1883)

    return client