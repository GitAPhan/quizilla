<template>
    <div>
        <quiz-screen></quiz-screen>
        <!-- <section>
        <h1>the question</h1>
        </section>
        <section>
            <button>1</button>
            <button>2</button>
            <button>3</button>
            <button>4</button>
        </section> -->
        <!-- <button ref="start_quiz" @click="load_quiz_page">START</button> -->

    </div>
</template>

<script>
import Cookies from "vue-cookies"
import QuizScreen from '@/components/QuizScreen.vue';

    export default {
  components: { QuizScreen },
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
section {
    display: grid;
    grid-row: auto;
}

</style>

