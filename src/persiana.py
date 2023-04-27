from connection import Connection

class persiana:

    def __init__(self, obert: bool, sensorId: str, location: str):
        self.obert = obert
        self.location = location
        self.sensorId = sensorId
        self.connection = Connection(sensorId, f'data/{self.location}/llum/{self.sensorId}')
        self.connection.client.on_message = self.on_message

    def obrirPersiana(self):
        self.obert = True;
        return self.obert

    def tencarPersiana(self):
        self.obert = False
        return self.obert

    def on_message(self, client, userdata, message):
        print(message.payload)

    def connect(self):
        self.connection.connect(f'command/{self.location}/llum/{self.sensorId}')
        self.connection.client.loop_forever()