if __name__ == '__main__':
    pass

llista_id_llums_menjador = [1, 2, 3]
llista_id_llums_cuina = [1, 2]
llista_id_llums_lavabo = [1, 2]
llista_id_llums_habitacio1 = [1]
llista_id_llums_habitacio2 = [1]

llista_id_temperatura_menjador = [1]
llista_id_temperatura_cuina = [1]
llista_id_temperatura_lavabo = [1]
llista_id_temperatura_habitacio1 = [1]
llista_id_temperatura_habitacio2 = [1]

llista_id_persianes_menjador = [1, 2]
llista_id_persianes_cuina = [1]
llista_id_persianes_lavabo = [1]
llista_id_persianes_habitacio1 = [1]


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


def triar_id_sensor(llista_id_llums_menjador, llista_id_llums_cuina, llista_id_llums_lavabo, llista_id_llums_habitacio1,
                    llista_id_llums_habitacio2, llista_id_temperatura_menjador, llista_id_temperatura_lavabo,
                    llista_id_temperatura_habitacio1, llista_id_temperatura_habitacio2, llista_id_persianes_menjador,
                    llista_id_persianes_cuina, llista_id_persianes_lavabo, llista_id_persianes_habitacio1,
                    localitzacio, tipus_sensor):

    if localitzacio == 1 & tipus_sensor == 1:
        print(llista_id_llums_menjador)
        while True:
            id_sensor_menjador_llum = int(input("Tria l'id del sensor: "))
            if id_sensor_menjador_llum in llista_id_llums_menjador:
                return id_sensor_menjador_llum
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 1 & tipus_sensor == 2:
        print(llista_id_temperatura_menjador)
        while True:
            id_sensor_menjador_temperaura = int(input("Tria l'id del sensor: "))
            if id_sensor_menjador_temperaura in llista_id_temperatura_menjador:
                return id_sensor_menjador_temperaura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 1 & tipus_sensor == 3:
        print(llista_id_persianes_menjador)
        while True:
            id_sensor_menjador_persianes = int(input("Tria l'id del sensor: "))
            if id_sensor_menjador_persianes in llista_id_persianes_menjador:
                return id_sensor_menjador_persianes
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 2 & tipus_sensor == 1:
        print(llista_id_llums_cuina)
        while True:
            id_sensor_cuina_llum = int(input("Tria l'id del sensor: "))
            if id_sensor_cuina_llum in llista_id_llums_cuina:
                return id_sensor_cuina_llum
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 2 & tipus_sensor == 2:
        print(llista_id_temperatura_cuina)
        while True:
            id_sensor_cuina_temperaura = int(input("Tria l'id del sensor: "))
            if id_sensor_cuina_temperaura in llista_id_temperatura_cuina:
                return id_sensor_cuina_temperaura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 2 & tipus_sensor == 3:
        print(llista_id_persianes_cuina)
        while True:
            id_sensor_cuina_persianes = int(input("Tria l'id del sensor: "))
            if id_sensor_cuina_persianes in llista_id_persianes_cuina:
                return id_sensor_cuina_persianes
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 3 & tipus_sensor == 1:
        print(llista_id_llums_lavabo)
        while True:
            id_sensor_lavabo_llum = int(input("Tria l'id del sensor: "))
            if id_sensor_lavabo_llum in llista_id_llums_lavabo:
                return id_sensor_lavabo_llum
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 3 & tipus_sensor == 2:
        print(llista_id_temperatura_lavabo)
        while True:
            id_sensor_lavabo_temperaura = int(input("Tria l'id del sensor: "))
            if id_sensor_lavabo_temperaura in llista_id_temperatura_lavabo:
                return id_sensor_lavabo_temperaura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 3 & tipus_sensor == 3:
        print(llista_id_persianes_lavabo)
        while True:
            id_sensor_lavabo_persianes = int(input("Tria l'id del sensor: "))
            if id_sensor_lavabo_persianes in llista_id_persianes_lavabo:
                return id_sensor_lavabo_persianes
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 4 & tipus_sensor == 1:
        print(llista_id_llums_habitacio1)
        while True:
            id_sensor_habitacio1_llum = int(input("Tria l'id del sensor: "))
            if id_sensor_habitacio1_llum in llista_id_llums_habitacio1:
                return id_sensor_habitacio1_llum
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 4 & tipus_sensor == 2:
        print(llista_id_temperatura_habitacio1)
        while True:
            id_sensor_habitacio1_temperaura = int(input("Tria l'id del sensor: "))
            if id_sensor_habitacio1_temperaura in llista_id_temperatura_habitacio1:
                return id_sensor_habitacio1_temperaura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 4 & tipus_sensor == 3:
        print(llista_id_persianes_habitacio1)
        while True:
            id_sensor_habitacio1_persianes = int(input("Tria l'id del sensor: "))
            if id_sensor_habitacio1_persianes in llista_id_persianes_habitacio1:
                return id_sensor_habitacio1_persianes
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 5 & tipus_sensor == 1:
        print(llista_id_llums_habitacio2)
        while True:
            id_sensor_habitacio2_llum = int(input("Tria l'id del sensor: "))
            if id_sensor_habitacio2_llum in llista_id_llums_habitacio2:
                return id_sensor_habitacio2_llum
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif localitzacio == 5 & tipus_sensor == 2:
        print(llista_id_temperatura_habitacio2)
        while True:
            id_sensor_habitacio2_temperaura = int(input("Tria l'id del sensor: "))
            if id_sensor_habitacio2_temperaura in llista_id_temperatura_habitacio2:
                return id_sensor_habitacio2_temperaura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    else:
        print("Opció incorrecta")


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
                return accio_llum
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
                return accio_temperatura
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    elif tipus_sensor == 3:
        print("""
                    Acció persiana:
                    1 - Pujar persiana
                    2 - Baixar persiana
                    """)
        while True:
            accio_persiana = int(input("Tria l'acció de la persiana: "))
            if accio_persiana in range(1, 3):
                return accio_persiana
            else:
                print("El valor introduït ha d'estar dins el rang de les opcions indicades.")
                continue

    else:
        print("Opció incorrecta.")
        return


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
        id_sensor = triar_id_sensor(llista_id_llums_menjador, llista_id_llums_cuina, llista_id_llums_lavabo,
                                    llista_id_llums_habitacio1, llista_id_llums_habitacio2,
                                    llista_id_temperatura_menjador, llista_id_temperatura_lavabo,
                                    llista_id_temperatura_habitacio1, llista_id_temperatura_habitacio2,
                                    llista_id_persianes_menjador, llista_id_persianes_cuina, llista_id_persianes_lavabo,
                                    llista_id_persianes_habitacio1, localitzacio, tipus_sensor)
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
