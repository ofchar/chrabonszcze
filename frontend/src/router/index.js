/* eslint-disable */
import Home from '../pages/HomePage.vue';
import Login from '../pages/LoginPage.vue';
import Register from '../pages/RegisterPage.vue';
import Settings from '../pages/SettingsPage.vue';

let routes = [
    {
        path: '/',
        component: Home,
    },
    {
        path: '/login',
        component: Login,
    },
    {
        path: '/register',
        component: Register,
    },
    {
        path: '/settings',
        component: Settings,
    }
]




export default routes