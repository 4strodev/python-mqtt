<script setup lang="ts">
import {MqttService} from './services/mqtt.service.ts';
import {onMounted, ref} from 'vue';

const mqttService = new MqttService("localhost", 9001, "Client_control_panel");

onMounted(connect)

async function connect() {
    console.log('Connecting to mqtt');
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
        mqttService.subscribe('Data/#');
    } catch (err) {
        console.error(err);
    }
}
const locations = ["Menjador", "Cuina", "Lavabo", "Habitacio_1", "Habitacio_2"]
const sensors = ["Llum", "Temperatura", "Persiana"]

const sensorId = ref("");
const location = ref<string>();
const sensorType = ref<string>();

const sensorAction = ref<string>();
const degrees = ref<number>();

const sensorActions = {
    "Llum": ["on", "off"],
    "Persiana" : ["open", "close"],
    "Temperatura" : ["increase", "decrease", "set"]
}

function sendData() {
    console.log(sensorId.value, location.value, sensorType.value, sensorAction.value, degrees.value)
    mqttService.client.send(``)
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

    <div v-for="action of sensorActions[sensorType]">
        <input type="radio" :id="action" :name="`accions_${sensorType}`" v-model="sensorAction" :value="action">
        <label for="html">{{ action }}</label><br>
    </div>

    <input type="number" v-if="sensorAction == 'set'" v-model="degrees">
</template>

<style scoped>
</style>
