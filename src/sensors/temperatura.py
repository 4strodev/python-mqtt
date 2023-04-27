import json

from src.connection.connection import Connection

class Temperatura:

    def __init__(self, graus: int, sensorId: str, location: str):
        self.graus = graus
        self.location = location
        self.sensorId = sensorId
        self.connection = Connection(sensorId, f'data/{self.location}/llum/{self.sensorId}')
        self.connection.client.on_message = self.on_message

    def pujar_temperatura(self, graus):
        self.graus = graus+1;
        self.notify_state()

    def baixar_temperatura(self, graus):
        self.graus = graus-1;
        self.notify_state()

    def establir_temperatura(self, temperatura):
        self.graus = temperatura
        self.notify_state()

    def notify_state(self):
        data = {
            "sensorId": self.sensorId,
            "location": self.location,
            "data": self.graus,
            "sensor": "termometre"
        }
        # json dumps el que fa es convertir un diccionari a un string
        self.connection.send_data(json.dumps(data))

    def on_message(self, client, userdata, message):
        print(message.payload)

    def connect(self):
        self.connection.connect(f'command/{self.location}/temperatura/{self.sensorId}')
        self.connection.client.loop_forever()