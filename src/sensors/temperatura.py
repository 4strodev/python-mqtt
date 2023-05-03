import json
from .sensor import Sensor

class Temperatura(Sensor):

    def __init__(self, graus: int, sensor_id: str, location: str):
        super().__init__(sensor_id=sensor_id, location=location, sensor_type='temperatura')
        self.graus = graus


    def pujar_temperatura(self, graus):
        self.graus = graus+1
        self.notify_state()

    def baixar_temperatura(self, graus):
        self.graus = graus-1
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
        print(message.payload)
