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
                        <input>
                    </div>
                    <div class="d-flex flex-column">
                        <label>Password</label>
                        <input>
                    </div>
                    <div class="w-100 d-flex mt-4">
                        <button class="button-custom" style="margin-left: auto;">Login</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {

}
</script>
<style>
@import '../css/login.css'
</style>