import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
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

export default router
