from sensors.llum import Llum
import concurrent.futures

def connect_sensors(sensors: list):
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(sensors)) as executor:
        for sensor in sensors:
            futures.append(executor.submit(sensor.connect))

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)

if __name__ == "__main__":
    llum = Llum(False, '1', 'Menjador')
    llum2 = Llum(False, '2', 'Menjador')

    sensors = [llum, llum2]
    connect_sensors(sensors)