from abc import abstractmethod

from connection.connection import Connection

class Sensor():
    def __init__(self, sensor_id: str, location: str, sensor_type: str):
        self.sensor_id = sensor_id
        self.location = location
        self.sensor_type = sensor_type

        self.base_topic = f'{self.location}/{self.sensor_type}/{self.sensor_id}'
        self.connection = Connection(self.sensor_id, f'data/{self.base_topic}')

        self.connection.client.on_message = self.on_message

    @abstractmethod
    def on_message(self,  client, userdata, message):
        pass

    async def connect(self):
        self.connection.connect(f'command/{self.base_topic}')
        self.connection.client.loop_forever()
