if __name__ == '__main__':
    pass

opcio = ''

def mostrar_menu():
    print("""MENÚ:
    1 - Triar localització
    2 - Triar sensor
    3 - Triar acció
    0 - Sortir""")

def triar_localitzacio():
    print("""
    1 - Menjador
    2 - Cuina
    3 - Lavabo
    4 - Habitacio1
    5 - Habitacio2
    0 - Sortir
    """)

def triar_tipus_sensor():
    print("""
    1 - Llum
    2 - Temperatura
    3 - Persiana
    0 - Sortir
    """)

def triar_id_sensor():
    id_sensor = int(input("Tria l'id del sensor: "))
    return id_sensor

def triar_accio_llum():
    print("""
    1 - Encendre llum
    2 - Apagar llum
    0 - Sortir
    """)

def triar_accio_persiana():
    print("""
    1 - Pujar persiana
    2 - Baixar persiana
    0 - Sortir
    """)

def triar_accio_temperatura():
    print("""
    1 - Pujar temperatura
    2 - Baixar temperatura
    3 - Establir temperatura
    0 - Sortir
    """)