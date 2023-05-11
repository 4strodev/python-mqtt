<script setup lang="ts">
import ReactiveInput from './components/ReactiveInput.vue'
import NavigationBar from "./components/NavigationBar.vue";
import {MqttService} from './services/mqtt.service.ts';
import {onMounted} from 'vue';

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

onMounted(connect);
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
