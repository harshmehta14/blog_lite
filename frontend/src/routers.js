import {createRouter, createWebHistory} from 'vue-router'
import HomePage from './components/HomePage'
import LoginPage from './components/LoginPage'
import SignupPage from './components/SignupPage.vue'

const routes = [
    {
        path:'/',
        name:'home',
        component:HomePage  
    },
    {
        path:'/login',
        name:'login',
        component:LoginPage  
    },
    {
        path:'/signup',
        name:'signup',
        component:SignupPage  
    },
    // {
    //     path:'/hello',
    //     name:'Hello',
    //     component:Hello    
    // },
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;