<template>
    <div :class="size == 2 ? 'image-big-container' : 'image-small-container'">
        <img class="image" :src="url" />
    </div>
</template>
<script>
export default {
    props: {
        url: null,
        size: { default: 2 },
    }
}
</script>

<style>
.image-big-container {
    height: 300px;
    width: 300px;
}

.image-small-container {
    height: 100px;
    width: 100px;
}

.image {
    width: 100%;
    height: 100%;
}
</style>