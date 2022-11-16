<template>
    <div class="d-flex justify-content-center h-100">
        <div class="d-flex flex-column justify-content-center w-100 h-100" style="max-width: 500px;">
            <div class="login-card card">
                <div class="card-header">
                    <h3 class="mb-0">Login</h3>
                </div>
                <div class="card-body p-4 row">
                    <div class="d-flex flex-column mb-4">
                        <label>Email</label>
                        <input v-model="email">
                    </div>
                    <div class="d-flex flex-column">
                        <label>Password</label>
                        <input v-model="password" type="password">
                    </div>
                    <div class="w-100 d-flex mt-4">
                        <button v-on:click="$router.push({ path: '/register' })" class="button-custom"
                            style="margin-right: auto;">Register</button>
                        <button v-on:click="login()" class="button-custom" style="margin-left: auto;">Login</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Swal from 'sweetalert2/dist/sweetalert2.js'
import 'sweetalert2/src/sweetalert2.scss'
export default {
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        login() {
            console.log('LOGIN')
            this.axios.post('http://localhost:5000/login', {
                'email': this.email,
                'password': this.password,
            }).then(response => {
                if (response.status == 200) {
                    localStorage.setItem('user', JSON.stringify(response.data))
                    localStorage.setItem('_token', response.data.token)
                    this.$nextTick(() => {
                        location.reload()
                    })
                }
                else {

                }
            }).catch(error => {
                console.log(error)
                Swal.fire({
                    title: 'Error!',
                    text: error.response.data,
                    icon: 'error',
                    confirmButtonText: 'Cool'
                })
            })
        }
    }

}
</script>
<style>
@import '../css/login.css'
</style>