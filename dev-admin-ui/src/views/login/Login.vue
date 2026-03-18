<template>
  <el-card class="login-box">
    <template #header>登录</template>
    <el-form label-width="auto">
      <el-form-item label="账号" class="form-item">
        <el-input v-model="state.form.username" placeholder="请输入账号" />
      </el-form-item>
      <el-form-item label="密码" class="form-item">
        <el-input
          v-model="state.form.password"
          type="password"
          placeholder="请输入密码"
          show-password />
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="footer">
        <el-button type="primary" @click="login">登录</el-button>
      </div>
    </template>
  </el-card>
</template>

<script setup>
  import { reactive, onUnmounted } from 'vue'
  import { ElMessage } from 'element-plus'
  import { useRouter } from 'vue-router'
  import useAxios from '../../hooks/useAxios'
  import { useEventListener } from '@vueuse/core'

  const http = useAxios()
  const router = useRouter()

  const state = reactive({
    form: {
      username: '',
      password: '',
    },
  })

  const cleanup = useEventListener('keydown', e => {
    if (e.key === 'Enter') {
      login()
    }
  })

  onUnmounted(() => {
    cleanup()
  })

  const login = async () => {
    const res = await http.post('/api/admin/auth/login', state.form)
    if (res.data.success) {
      const token = res.data.data
      sessionStorage.setItem('token', token)
      router.push('/home')
    } else {
      ElMessage.error(res.data.message)
    }
  }
</script>

<style scoped lang="scss">
  .login-box {
    width: 450px;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    .footer {
      display: flex;
      justify-content: end;
    }
  }
</style>
