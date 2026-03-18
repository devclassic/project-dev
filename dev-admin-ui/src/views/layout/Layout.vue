<template>
  <div class="layout">
    <Sidebar />
    <div class="main">
      <router-view />
    </div>
  </div>
</template>

<script setup>
  import Sidebar from './Sidebar.vue'
</script>

<style scoped lang="scss">
  .layout {
    height: 100vh;
    display: flex;
  }

  .main {
    flex: 1;
    min-width: 0;
    padding: 0 10px;
  }
</style>
