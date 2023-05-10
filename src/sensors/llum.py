import json
from .sensor import Sensor


class Llum(Sensor):
    def __init__(self, sensorId: str, location: str):
        super().__init__(sensorId, location, 'Llum')
        self.obert = False

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
        arrayString = message.payload.decode()
        diccionari = json.load(arrayString)
        print(type(message.payload))
        print("prova correcte")
        print(diccionari)
