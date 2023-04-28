def triar_localitzacio():
    print("""
    Localització:
    1 - Menjador
    2 - Cuina
    3 - Lavabo
    4 - Habitacio1
    5 - Habitacio2
    """)
    while True:
        localitzacio = int(input("Tria la localització:"))
        if localitzacio in range(1, 6):
            return localitzacio
        else:
            print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
            continue


def triar_tipus_sensor():
    print("""
    Tipus sensor: 
    1 - Llum
    2 - Temperatura
    3 - Persiana
    """)
    while True:
        tipus_sensor = int(input("Tria el tipus de sensor:"))
        if tipus_sensor in range(1, 4):
            return tipus_sensor
        else:
            print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
            continue


def seleccionar_id_sensor():
    return int(input("Introdueix l'id del sensor: "))

def triar_accio_sensor(tipus_sensor):
    if tipus_sensor == 1:
        print("""
        Acció llum:
        1 - Encendre llum
        2 - Apagar llum
        """)
        while True:
            accio_llum = int(input("Tria l'acció del llum: "))
            if accio_llum in range(1, 3):
                if (accio_llum == 1):
                    return "on"
                else:
                    return "off"
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif tipus_sensor == 2:
        print("""
                    Acció temperatura:
                    1 - Pujar temperatura
                    2 - Baixar temperatura
                    3 - Establir temperatura
                    """)
        while True:
            accio_temperatura = int(input("Tria l'acció de la temperatura: "))
            if accio_temperatura in range(1, 4):
                if (accio_temperatura == 1):
                    return "increase"
                elif (accio_temperatura == 2):
                    return "decrease"
                else:
                    graus = int(input("Estableix la temperatura desitjada: "))
                    return "set", graus
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif tipus_sensor == 3:
        print("""
                    Acció persiana:
                    1 - Obrir persiana
                    2 - Tancar persiana
                    """)
        while True:
            accio_persiana = int(input("Tria l'acció de la persiana: "))
            if accio_persiana in range(1, 3):
                if (accio_persiana == 1):
                    return "open"
                else:
                    return "close"
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    else:
        print("Opció incorrecta.")
        return

def seleccionar_informacio_sensor():
    localitzacio = ''
    tipus_sensor = ''
    id_sensor = ''
    accio_sensor = ''

    while True:
        try:
            localitzacio = triar_localitzacio()
            break
        except ValueError:
            print("El valor introduït ha de ser un número enter.")
            continue

    while True:
        try:
            tipus_sensor = triar_tipus_sensor()
            break
        except ValueError:
            print("El valor introduït ha de ser un número enter.")
            continue

    while True:
        try:
            id_sensor = seleccionar_id_sensor()
            break
        except ValueError:
            print("El valor introduït ha de ser un número enter.")
            continue

    while True:
        try:
            accio_sensor = triar_accio_sensor(tipus_sensor)
            break
        except ValueError:
            print("El valor introduït ha de ser un número enter.")
            continue

    return localitzacio, tipus_sensor, id_sensor, accio_sensor


if __name__ == '__main__':
    while True:
        localitzacio, tipus_sensor, id_sensor, accio_sensor = seleccionar_informacio_sensor()
