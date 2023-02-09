<template>
    <div>
        <button ref="start_quiz" @click="load_quiz_page">START</button>

    </div>
</template>

<script>
import Cookies from "vue-cookies"

    export default {
        mounted () {
            Cookies.get('points');
        },
        data() {
            return {
                user_cookie: {
                    'points': 0
            }
        }
        },

        name: 'start-page'
        
    }
</script>

<style lang="scss" scoped>

</style>