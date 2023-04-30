import json

from connection.connection import Connection


class Llum:

    def __init__(self, obert: bool, sensorId: str, location: str):
        self.obert = obert
        self.location = location
        self.sensorId = sensorId
        self.connection = Connection(sensorId, f'data/{self.location}/llum/{self.sensorId}')
        self.connection.client.on_message = self.on_message

    def obrir_llum(self):
        self.obert = True
        self.notify_state()

    def tencar_llum(self):
        self.obert = False
        self.notify_state()

    def notify_state(self):
        data = {
            "data": self.obert,
        }
        # json dumps el que fa es convertir un diccionari a un string
        self.connection.send_data(json.dumps(data))

    def on_message(self, client, userdata, message):
        print(message.payload)

    def connect(self):
        self.connection.connect(f'command/{self.location}/llum/{self.sensorId}')
        self.connection.client.loop_forever()
