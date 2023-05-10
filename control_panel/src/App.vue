<script setup lang="ts">
import ReactiveInput from './components/ReactiveInput.vue'
import NavBar from "./components/NavigationBar.vue";
import NavigationBar from "./components/NavigationBar.vue";
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
