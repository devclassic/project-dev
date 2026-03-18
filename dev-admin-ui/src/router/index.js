import { createRouter, createWebHashHistory } from 'vue-router'
import useAxios from '../hooks/useAxios'

const http = useAxios()

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/login',
      component: () => import('../views/login/Login.vue'),
    },
    {
      path: '/',
      component: () => import('../views/layout/Layout.vue'),
      children: [
        {
          path: '/home',
          component: () => import('../views/home/Home.vue'),
        },
        {
          path: '/dev/list',
          component: () => import('../views/dev/list/List.vue'),
        },
      ],
    },
  ],
})

router.beforeEach(async to => {
  const token = sessionStorage.getItem('token')
  const res = await http.post('api/admin/auth/check')
  if (to.path !== '/login') {
    if (!token || !res.data.success) {
      return '/login'
    }
  } else {
    return true
  }
})

export default router
