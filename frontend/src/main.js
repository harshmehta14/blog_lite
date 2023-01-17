import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './routers'
import NavBar from './components/NavBar.vue'



const app = createApp(App)
app.use(router)
app.mount('#app')
app.component('NavBar', NavBar)
