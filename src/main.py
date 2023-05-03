import asyncio

from sensors.llum import Llum
from sensors.sensor import Sensor
import concurrent.futures



# async def connect_sensors(sensor_list: list[Sensor]) -> list[asyncio.Task]:
#     sensor_tasks: list[asyncio.Task] = []
#     with ThreadPoolExecutor() as pool:
#         for sensor in sensor_list:
#             future = asyncio.get_running_loop().run_in_executor(pool, sensor.connect())
#             task = asyncio.create_task(await future)
#             sensor_tasks.append(task)
#
#     return sensor_tasks

if __name__ == "__main__":
    llum = Llum(False, '1', 'Menjador')
    llum2 = Llum(False, '2', 'Menjador')

    sensors = [llum, llum2]
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(sensors)) as executor:
        for sensor in sensors:
            futures.append(executor.submit(sensor.connect))

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)

