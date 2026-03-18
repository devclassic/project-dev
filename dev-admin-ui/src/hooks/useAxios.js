import axios from 'axios'
import { ElMessageBox } from 'element-plus'
import router from '../router'

const http = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL ?? '',
})

http.interceptors.request.use(
  config => {
    const token = sessionStorage.getItem('token')
    if (token) {
      config.headers['token'] = token
    }
    return config
  },
  error => {
    return Promise.reject(error)
  },
)

http.interceptors.response.use(
  response => {
    if (response.data.code === 1001) {
      ElMessageBox.alert(response.data.message)
      router.push('/login')
    }
    return response
  },
  error => {
    return Promise.reject(error)
  },
)

export default () => {
  return http
}
