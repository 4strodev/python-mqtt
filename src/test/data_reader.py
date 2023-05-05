from sensor_data import config
from src.sensors.llum import Llum
from src.sensors.persiana import Persiana
from src.sensors.temperatura import Temperatura
from src.sensors.sensor import Sensor




def initialize_sensors(config) -> list[Sensor]:
    sensors: list[Sensor] = []

    for location in config:
        localitzacio = config.get(location)
        for tipus_sensor, quantitat in localitzacio.items():
            if tipus_sensor == "Llum":
                for i in range(quantitat):
                    sensor = Llum(f"{location, tipus_sensor, i}", location)
                    sensors.append(sensor)
            if tipus_sensor == "Temperatura":
                for i in range(quantitat):
                    sensor = Temperatura(f"{location, tipus_sensor, i}", location)
                    sensors.append(sensor)
            if tipus_sensor == "Persiana":
                for i in range(quantitat):
                    sensor = Persiana(f"{location, tipus_sensor, i}", location)
                    sensors.append(sensor)
    return sensors


if __name__ == '__main__':
    sensors: list[Sensor] = initialize_sensors(config)

    print(sensors)




