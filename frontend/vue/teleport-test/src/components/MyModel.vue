<script setup lang="ts">
const show = defineModel<boolean>("showModel");
</script>

<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="show" class="model-body">
        <div>
          <h1>This is Model</h1>
          <p>Good Idea From Here!</p>
        </div>
        <button v-on:click="show = false">Close</button>
      </div>
    </Transition>
  </Teleport>
</template>

<style lang="scss" scoped>
.model-body {
  background-color: rgba(93, 93, 93, 0.486);
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
}

// 下面是动画相关的东西，前面的modal就是上面Transition里面设置的 name 属性。
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
