<template>
    <div class="home-page-container">
        <h1>Quizzilla</h1>

        <img src="@/assets/godzilla.png" alt="quizilla" />

        <div class="btn-container"> 
            <start-game class="btn"></start-game>
            <add-question class="btn"></add-question>
        </div>

    </div>
</template>

<script>
import StartGame from '@/components/StartGame.vue'
import AddQuestion from '@/components/AddQuestion.vue'

    export default {
        // data() {
        //     return {
        //         godzilla: "https://img.pokemondb.net/sprites/sword-shield/icon/venusaur.png"
        //     }
        // },
        components: { StartGame, AddQuestion },
        name: 'home-page'
    }
</script>

<style lang="scss">
.home-page-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    h1 {
        color: #fff;
        // align-self: center;
        // justify-content: center;
    }
}
img {
    width: 200px;
    padding-bottom: 20px;

    @media screen and (min-width: 650px) {
        width: 300px;
    }
}
.btn-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>