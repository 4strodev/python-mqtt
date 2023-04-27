from connection import Connection

class temperatura:

    def __init__(self, graus: int, sensorId: str, location: str):
        self.graus = graus
        self.location = location
        self.sensorId = sensorId
        self.connection = Connection(sensorId, f'data/{self.location}/llum/{self.sensorId}')
        self.connection.client.on_message = self.on_message

    def pujarTemperatura(self,graus):
        self.graus = graus+1;
        return self.graus

    def baixarTemperatura(self,graus):
        self.graus = graus-1;
        return self.graus

    def establirTemperatura(self, temperatura):
        self.graus = temperatura
        return self.graus

    def on_message(self, client, userdata, message):
        print(message.payload)

    def connect(self):
        self.connection.connect(f'command/{self.location}/llum/{self.sensorId}')
        self.connection.client.loop_forever()