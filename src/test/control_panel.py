import json
import paho.mqtt.client as paho

def on_publish(client, userdata, result):
    print("data published \n")

def triar_localitzacio():
    localitzacions = [
        'Menjador',
        'Cuina',
        'Lavabo',
        'Habitacio1',
        'Habitacio2'
    ]
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
            return localitzacions[localitzacio - 1]
        else:
            print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
            continue


def triar_tipus_sensor():
    tipus_sensors = ['Llum', 'Temperatura', 'Persiana']
    print("""
    Tipus sensor: 
    1 - Llum
    2 - Temperatura
    3 - Persiana
    """)
    while True:
        tipus_sensor = int(input("Tria el tipus de sensor:"))
        if tipus_sensor in range(1, 4):
            return tipus_sensors[tipus_sensor - 1]
        else:
            print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
            continue


def seleccionar_id_sensor():
    return input("Introdueix l'id del sensor: ")

def triar_accio_sensor(tipus_sensor):
    if tipus_sensor == 'Llum':
        print("""
        Acció llum:
        1 - Encendre llum
        2 - Apagar llum
        """)
        while True:
            accio_llum = int(input("Tria l'acció del llum: "))
            if accio_llum in range(1, 3):
                if (accio_llum == 1):
                    return "on", None
                else:
                    return "off", None
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif tipus_sensor == 'Temperatura':
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
                    return "increase", None
                elif (accio_temperatura == 2):
                    return "decrease", None
                else:
                    graus = int(input("Estableix la temperatura desitjada: "))
                    return "set", graus
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif tipus_sensor == 'Persiana':
        print("""
                    Acció persiana:
                    1 - Obrir persiana
                    2 - Tancar persiana
                    """)
        while True:
            accio_persiana = int(input("Tria l'acció de la persiana: "))
            if accio_persiana in range(1, 3):
                if (accio_persiana == 1):
                    return "open", None
                else:
                    return "close", None
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

    # Crea un objecte client
    client = paho.Client("control1")
    # Assigna la funció callback
    client.on_publish = on_publish
    # Estableix la connexió
    client.connect('localhost', 1883)

    while True:
        localitzacio, tipus_sensor, id_sensor, accio_sensor = seleccionar_informacio_sensor()
        action, value = accio_sensor

        topic = f'Command/{localitzacio}/{tipus_sensor}/{id_sensor}'
        print(topic)
        json_action = json.dumps({'action': action})

        if (action == 'set'):
            json_action = json.dumps({'action': action, 'value': value})

        client.publish(topic, json_action)
