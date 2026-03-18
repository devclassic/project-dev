<template>
  <div class="sidebar">
    <el-menu
      :router="true"
      :default-active="route.path"
      text-color="#fff"
      active-text-color="#ffd04b"
      background-color="#545c64">
      <el-menu-item index="/home">起始页</el-menu-item>
      <el-sub-menu index="/dev">
        <template #title>开发模板</template>
        <el-menu-item index="/dev/list">列表模板</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'

  const route = useRoute()
</script>

<style scoped lang="scss">
  .sidebar {
    width: 200px;
    height: 100%;
    background-color: #545c64;
    overflow: auto;
  }

  :deep(.el-menu) {
    border-right: 0;
  }
</style>
