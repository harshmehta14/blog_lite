import {createRouter, createWebHistory} from 'vue-router'
import HomePage from './components/HomePage'
import LoginPage from './components/LoginPage'
import SignupPage from './components/SignupPage.vue'
import ProfilePage from './components/ProfilePage.vue'
import FollowerPage from './components/FollowerPage.vue'

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
    {
        path:'/profile',
        name:'profile',
        component:ProfilePage  
    },
    {
        path:'/follower',
        name:'follower',
        component:FollowerPage  
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