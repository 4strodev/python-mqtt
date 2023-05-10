<script setup lang="ts">
import SensorsNavigator from "./SensorsNavigator.vue";

const locations = ["Menjador","Cuina","Lavabo","Habitacio1","Habitacio2"]
</script>

<template>
<nav>
    <ul>
        <li v-for="location in locations">
            <h2>{{location}}</h2>
        </li>
    </ul>
</nav>
</template>

<style scoped>
li {
    list-style: none;
}
</style>