import json
from .sensor import Sensor


class Temperatura(Sensor):

    def __init__(self, sensor_id: str, location: str):
        super().__init__(sensor_id=sensor_id, location=location, sensor_type='Temperatura')
        self.graus = 0

    def pujar_temperatura(self, graus):
        self.graus = graus + 1
        self.notify_state()

    def baixar_temperatura(self, graus):
        self.graus = graus - 1
        self.notify_state()

    def establir_temperatura(self, temperatura):
        self.graus = temperatura
        self.notify_state()

    def notify_state(self):
        data = {
            "data": self.graus,
        }
        # json dumps el que fa es convertir un diccionari a un string
        self.connection.send_data(json.dumps(data))

    def on_message(self, client, userdata, message):
        arrayString = message.payload.decode()
        diccionari = json.loads(arrayString)
        if diccionari["action"] == "increase":
            self.pujar_temperatura(self.graus)
        if diccionari["action"] == "decrease":
            self.baixar_temperatura(self.graus)
        if diccionari["action"] == "set":
            self.establir_temperatura(diccionari["value"])
