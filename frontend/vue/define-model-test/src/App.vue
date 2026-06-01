<script setup lang="ts">
import MyDialog from "./components/MyDialog.vue";
import { ref } from "vue";

const showDialog = ref(false);
</script>

<template>
  <h1>Hello DefineModel!</h1>
  <p>A test for defineModel.</p>
  <button @click="showDialog = true">Show Dialog</button>
  <MyDialog v-model:show="showDialog"></MyDialog>
</template>
