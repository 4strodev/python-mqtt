<script setup lang="ts">
const sensors = ["Llum","Persiana","Temperatura"]

</script>

<template>
<nav>
    <header>
        <button v-for="sensors in sensors" style="white-space: nowrap">{{sensors}}</button>
    </header>

</nav>
</template>

<style scoped>

header {
    display: flex;
    flex-wrap: nowrap;
    width: 100%;
    justify-content: space-around;
}
button {
    padding: 1em;
}
</style>