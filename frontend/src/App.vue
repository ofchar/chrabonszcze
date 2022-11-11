<template>
    <navbar-component></navbar-component>
    <div class="container w-100 h-100" style="padding-top: 100px">
        <router-view></router-view>
    </div>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue';
export default {
    components: {
        NavbarComponent,
    }
}
</script>

<style>
@import './css/main.css'
</style>
