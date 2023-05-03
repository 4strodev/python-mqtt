import json
from .sensor import Sensor


class Persiana(Sensor):

    def __init__(self, obert: bool, sensorId: str, location: str):
        super().__init__(sensorId, location, 'persiana')
        self.obert = obert

    def obrir_persiana(self):
        self.obert = True;
        self.notify_state()

    def tencar_persiana(self):
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
