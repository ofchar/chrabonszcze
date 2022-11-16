<template>
    <navbar-component></navbar-component>
    <div class="container w-100 h-100" style="padding-top: 100px">
        <router-view></router-view>
    </div>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue';
export default {
    data() {
        return {

        }
    },
    components: {
        NavbarComponent,
    },
    methods: {
        middlware() {
            let _token = null
            _token = localStorage.getItem(_token);
            if (!_token) {
                if ((this.$route.path != '/login' && this.$route.path != '/register')) {
                    this.$router.push({ path: '/login' })
                }
            }
            else {
                if (this.$route.path == '/login' && this.$route.path == '/register') {
                    this.$router.push({ path: '/home' })
                }
            }

        }
    },
    watch: {
        '$route'() {
            this.middlware()
        }
    },
    mounted() {

    }
}
</script>

<style>
@import './css/main.css'
</style>
