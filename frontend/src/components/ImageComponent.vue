<template>
    <h3 v-if="size == 1">{{ type }}</h3>
    <div :class="size == 2 ? 'image-big-container' : 'image-small-container'">
        <h3 v-if="size == 2" class="image-desc">{{ type }}</h3>
        <img v-if="type == 'Happy'" class="image" src="../assets/good.png" />
        <img v-if="type == 'Very Happy'" class="image" src="../assets/very_good.png" />
        <img v-if="type == 'Sad'" class="image" src="../assets/sad.png" />
        <img v-if="type == 'Very Sad'" class="image" src="../assets/very_sad.png" />
    </div>
</template>
<script>
export default {
    data() {
        return {
            type: null
        }
    },
    props: {
        value: null,
        size: { default: 2 },
    },
    mounted() {
        if (this.value <= -0.5) {
            this.type = 'Very Sad'
        }
        if (this.value > -0.5 && this.value < 0) {
            this.type = 'Sad'
        }
        if (this.value >= 0 && this.value < 0.5) {
            this.type = 'Happy'
        }
        if (this.value >= 0.5) {
            this.type = 'Very Happy'
        }
    }
}
</script>

<style>
.image-big-container {
    position: relative;
    height: 300px;
    width: 300px;
    text-align: center;
}

.image-small-container {
    position: relative;
    height: 200px;
    width: 200px;
    text-align: center;
}

.image {
    border: 3px solid aqua;
    border-radius: 10px;
    width: 100%;
    height: 100%;
}

.image-desc {
    font-weight: bold;
    color: black;
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>