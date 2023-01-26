import {createRouter, createWebHistory} from 'vue-router'
import HomePage from './components/HomePage'
import LoginPage from './components/LoginPage'
import SignupPage from './components/SignupPage.vue'
import ProfilePage from './components/ProfilePage.vue'
import FriendsPage from './components/FriendsPage.vue'

import TestPage from './components/TestPage.vue'
import PostPage from './components/WritePostPage.vue'
import MyPostPage from './components/MyPostPage.vue'

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
        path:'/friends',
        name:'friends',
        component:FriendsPage  
    },
    {
        path:'/test',
        name:'test',
        component:TestPage  
    },
    {
        path:'/createpost',
        name:'createpost',
        component:PostPage  
    },
    {
        path:'/myposts',
        name:'mypost',
        component:MyPostPage  
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