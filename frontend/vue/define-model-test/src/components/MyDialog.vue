<script setup lang="ts">
const showDialog = defineModel<boolean>("show", { required: true });
</script>

<template>
  <Teleport to="body">
    <Transition>
      <div v-show="showDialog" class="dialog-container">
        <h1>This is Title</h1>
        <p>This is content</p>
        <button @click="showDialog = false">Close Dialog</button>
      </div>
    </Transition>
  </Teleport>
</template>

<style lang="css" scoped>
.dialog-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.192);
  backdrop-filter: blur(5px);
}
</style>
