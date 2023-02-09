<template>
    <div>
        <h1>Quizzilla</h1>
        <img src=godzilla alt="some lizard" />
        <start-game></start-game>
        <add-question></add-question>

        
        
        

    </div>
</template>

<script>
import StartGame from '@/components/StartGame.vue'
import AddQuestion from '@/components/AddQuestion.vue'

    export default {
        data() {
            return {
                godzilla: "https://img.pokemondb.net/sprites/sword-shield/icon/venusaur.png"
            }
        },
  components: { StartGame, AddQuestion },
        name: 'home-page'
    }
</script>

<style scoped>

</style>