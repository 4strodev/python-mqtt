<script setup lang="ts">
import ReactiveInput from './components/ReactiveInput.vue'
import NavigationBar from "./components/NavigationBar.vue";
import {MqttService} from './services/mqtt.service.ts';
import {onMounted, ref} from 'vue';

async function connect() {
    console.log('Connecting to mqtt');
    const mqttService = new MqttService("localhost", 9001, "Client_control_panel");
    try {
        await mqttService.connect();
        console.log('connected')
    } catch (err) {
        console.error(err);
        return;
    }

    mqttService.onMessage((message) => {
        console.log(message)
    });

    try {
        mqttService.subscribe('Data/Menjador/Llum/Menjador_Llum_1');
    } catch (err) {
        console.error(err);
    }
}
const locations = ["Menjador", "Cuina", "Lavabo", "Habitacio_1", "Habitacio_2"]
const sensors = ["Llum", "Temperatura", "Persiana"]

const sensorId = ref("");
const location = ref<string>();
const sensorType = ref<string>();

function sendData() {
    console.log(sensorId.value, location.value, sensorType.value)
}

// onMounted(connect);
</script>

<template>
    <input type="text" v-model="sensorId">
    <select name="select" v-model="location">
        <option v-for="location of locations" :value="location">{{location}}</option>
    </select>
    <select name="select" v-model="sensorType">
        <option v-for="sensor of sensors" :value="sensor">{{sensor}}</option>
    </select>
    <button @click="sendData">Send command</button>
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

#Nav {
    margin-top: 0px;

}

</style>
