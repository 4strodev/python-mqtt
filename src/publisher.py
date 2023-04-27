import paho.mqtt.client as paho
broker = "localhost"
port = 1883
# Crea la funció per callback. La funció que s'executa quan es produeix l'event on_publish


def on_publish(client, userdata, result):
    print("data published \n")


# Crea un objecte client
client1 = paho.Client("control1")
# Assigna la funció callback
client1.on_publish = on_publish
# Estableix la connexió
client1.connect(broker, port)
# Fa una publicacio
ret = client1.publish("command/Menjador/llum/1", "on")
if ret[0] == 0:
    print("El topic s'ha enviat correctament!")
else:
    print("S'ha produït un error a l'hora d'enviar el topic")
