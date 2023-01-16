import {createRouter, createWebHistory} from 'vue-router'
import HomePage from './components/HomePage'
import Hello from './components/HelloWorld'

const routes = [
    {
        path:'/',
        name:'home',
        component:HomePage  
    },
    {
        path:'/hello',
        name:'Hello',
        component:Hello    
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;