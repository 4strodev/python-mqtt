import concurrent.futures
from sensors.sensor import Sensor
from sensors.llum import Llum
from sensors.persiana import Persiana
from sensors.temperatura import Temperatura
from test.sensor_data import config

def initialize_sensors(config) -> list[Sensor]:
    sensors: list[Sensor] = []

    for location in config:
        localitzacio = config.get(location)
        for tipus_sensor, quantitat in localitzacio.items():
            if tipus_sensor == "Llum":
                for i in range(quantitat):
                    sensor = Llum(f"{location}_{tipus_sensor}_{i}", location)
                    sensors.append(sensor)
            if tipus_sensor == "Temperatura":
                for i in range(quantitat):
                    sensor = Temperatura(f"{location}_{tipus_sensor}_{i}", location)
                    sensors.append(sensor)
            if tipus_sensor == "Persiana":
                for i in range(quantitat):
                    sensor = Persiana(f"{location}_{tipus_sensor}_{i}", location)
                    sensors.append(sensor)

    return sensors
def connect_sensors(sensors: list):
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(sensors)) as executor:
        for sensor in sensors:
            futures.append(executor.submit(sensor.connect))

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)

if __name__ == "__main__":
    sensors = initialize_sensors(config)
    connect_sensors(sensors)
