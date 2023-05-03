import paho.mqtt.client as paho

class Connection:
    broker = "localhost"
    port = 1883

    def __init__(self, clientId: str, dataTopic: str):
        self.client = paho.Client(clientId)
        self.dataTopic = dataTopic

    def connect(self, topic):
        self.client.connect(self.broker, self.port)

        def on_connect(client, userdata, flags, rc):
            print('connected (%s)' % client._client_id)
            client.subscribe(topic=topic, qos=2)

        self.client.on_connect = on_connect

    def send_data(self, data):
        response = self.client.publish(self.dataTopic, data)
        if response[0] != 0:
            raise Exception("Hi ha hagut un error a l'enviar el missatge.")
