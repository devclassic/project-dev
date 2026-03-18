import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import './assets/css/global.scss'
import 'element-plus/dist/index.css'
import App from './App.vue'

const pinia = createPinia()

const app = createApp(App)
app.use(router)
app.use(pinia)
app.use(ElementPlus, { locale: zhCn })
app.mount('#app')
