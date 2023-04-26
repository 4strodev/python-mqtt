import paho.mqtt.client as paho
"""
Que ha de fer la connexio

Connectarse al broker
Suscriures a un topic
    Permetre rebre la funcio on message per saber que ha de fer quen rep un missatge
Enviar informacio a un topic
"""
class Connection:
    broker = "localhost"
    port = 1883

    def __init__(self, clientId: str):
        self.client = paho.Client(clientId)

    def connect(self, topic):
        self.client.connect(self.broker, self.port)

        def on_connect(client, userdata, flags, rc):
            print('connected (%s)' % client._client_id)
            client.subscribe(topic=topic, qos=2)

        self.client.on_connect = on_connect
