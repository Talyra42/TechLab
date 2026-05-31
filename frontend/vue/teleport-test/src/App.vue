<script setup lang="ts">
import MyModel from "./components/MyModel.vue";
import { ref } from "vue";

const showModel = ref(false);
</script>

<template>
  <h1>Teleport 测试</h1>
  <button v-on:click="showModel = !showModel">打开Model</button>
  <MyModel v-model:show-model="showModel"></MyModel>
</template>
