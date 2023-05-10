<script setup lang="ts">
import ReactiveInput from './components/ReactiveInput.vue'
import NavigationBar from "./components/NavigationBar.vue";
declare let Paho: any;
const client = new Paho.MQTT.Client("localhost", 9001, "client_tu_puta_madre");
function onConnectionLost() {
    console.log('connection lost')
}
//S'executa si no  s'ha pogut connectar al servidor
function onFailure(message) {
    console.log('failure')
}
//S'executa quan arriba un missatge
function onMessageArrived(r_message) {
    console.log('message arrived');
    console.log(r_message);
    console.log(r_message.payloadString)
}

function onConnected() {

}

client.onConnectionLost = onConnectionLost;
client.onFailure = onFailure;
client.onMessageArrived = onMessageArrived;
client.onConnected = onConnected;

function onConnect() {
    client.subscribe('Data/Menjador/Llum/Menjador_Llum_1');
    console.log('connect');
}

var options = {
    timeout: 3,
    cleanSession: true,
    onSuccess: onConnect,
    onFailure: onFailure,

};
client.connect(options);

</script>

<template>
  <ReactiveInput msg="Vite + Vue" />
  <NavigationBar></NavigationBar>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
