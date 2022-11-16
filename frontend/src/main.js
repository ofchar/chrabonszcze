import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router'
import routes from '../src/router';
import Axios from 'axios'

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`
});

import 'bootstrap/dist/css/bootstrap.css';

const app = createApp(App)

app.config.globalProperties.axios = Axios;

app.use(router);

app.mount('#app');
