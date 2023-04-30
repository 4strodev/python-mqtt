from sensors.llum import Llum

if __name__ == "__main__":
    llum1 = Llum(False, '1', 'Menjador')
    llum1.connect()
    llum2 = Llum(False, '2', 'Menjador')
    llum2.connect()
