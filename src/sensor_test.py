from src.sensors.llum import Llum

if __name__ == '__main__':
    sensor = Llum(False, '1', 'Menjador')
    sensor.connect()
