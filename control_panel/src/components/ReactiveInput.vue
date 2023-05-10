<script setup lang="ts">
import {ref} from "vue"
let contingutTitol = ref("Contingut del Titol")

</script>

<template>
    <h1>{{contingutTitol}}</h1>
    <input type="text" v-model="contingutTitol">
</template>

<style scoped>

</style>