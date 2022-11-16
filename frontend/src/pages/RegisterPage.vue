<template>
    <div class="d-flex justify-content-center h-100">
        <div class="d-flex flex-column justify-content-center w-100 h-100" style="max-width: 500px;">
            <div class="login-card card">
                <div class="card-header">
                    <h3 class="mb-0">Register</h3>
                </div>
                <div class="card-body p-4 row">
                    <div class="d-flex flex-column mb-4">
                        <label>Email</label>
                        <input v-model="email">
                    </div>
                    <div class="d-flex flex-column mb-4">
                        <label>Name</label>
                        <input v-model="name">
                    </div>
                    <div class="d-flex flex-column mb-4">
                        <label>Password</label>
                        <input v-model="password" type="password">
                    </div>
                    <div class="d-flex flex-column">
                        <label>Repeat password</label>
                        <input v-model="rePassword" type="password">
                    </div>
                    <div class="w-100 d-flex mt-4">
                        <button v-on:click="$router.push({ path: '/login' })" class="button-custom"
                            style="margin-right: auto;">Login</button>
                        <button v-on:click="register()" class="button-custom"
                            style="margin-left: auto;">Register</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            email: '',
            name: '',
            password: '',
            rePassword: ''
        }
    },
    methods: {
        register() {
            this.axios.post('http://localhost:5000/register', {
                'name': this.name,
                'email': this.email,
                'password': this.password,
            }).then(response => {
                if (response.status == 201) {
                    this.$router.push({ path: '/login' })
                }
            })
        }
    }
}
</script>
<style>
@import '../css/login.css'
</style>