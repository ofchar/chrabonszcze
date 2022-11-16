<template>
    <div class="navbar-container">
        <div class="custom-navbar-left">
            <div class="d-flex" style="gap: 20px">
                <button class="button-custom">Home</button>
            </div>
        </div>
        <div class="custom-navbar-right">
            <div class="d-flex" style="gap: 20px;">
                <button v-on:click="logout()" v-if="_token && _token != 'null'" class="button-custom">Logout</button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            _token: localStorage.getItem('_token')
        }
    },
    methods: {
        logout() {
            this.axios.post('http://localhost:5000/logout', {
                'token': this._token
            }).then(response => {
                localStorage.setItem('user', null)
                localStorage.setItem('_token', null)
                location.reload()
            })
        }
    }

}
</script>
<style>
@import '../css/navbar.css';
</style>