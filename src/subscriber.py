import paho.mqtt.client
import ssl
import sys
broker = "192.168.17.169"
port = 1883
topic = 'Command/Menjador/Llum/1'


# Crea la funció per callback. La funció que s'executa quan es produeix l'event de client connectat

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    # Subscriu a un topic
    client.subscribe(topic=topic, qos=2)

def on_disconnect(client, userdata, rc):
    print('disconnected (%s)' % client._client_id)

# Crea la funció per callback. La funció que s'executa quan es produeix l'event on_message. Ha arribat un missatges des del broker


def on_message(client, userdata, message):
    print('------------------------------')
    print('payload: %s' % message.payload)

# Defineix una funció d'inicialització


def main():
    client = paho.mqtt.client.Client(
        client_id='insplasll_1', clean_session=False)
    # Assigna les funcions callback
    client.on_connect = on_connect


    client.on_message = on_message
    client.on_disconnect = on_disconnect
    # Es connecta al broker
    client.connect(host=broker, port=port)
    client.loop_forever()


if __name__ == '__main__':
    main()

sys.exit(0)
