import asyncio

from sensors.llum import Llum
from sensors.sensor import Sensor


def connect_sensors(sensor_list: list[Sensor]) -> list[asyncio.Task]:
    sensor_tasks: list[asyncio.Task] = []
    for sensor in sensor_list:
        task = asyncio.create_task(sensor.connect())
        sensor_tasks.append(task)

    return sensor_tasks

async def main():
    llum = Llum(False, '1', 'Menjador')
    llum2 = Llum(False, '2', 'Menjador')

    sensor_tasks = connect_sensors([llum, llum2])

if __name__ == "__main__":
    asyncio.run(main())

