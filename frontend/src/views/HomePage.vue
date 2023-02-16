<template>
    <div>

        <img src="@/assets/godzilla.png" alt="some lizard" />
        <button>
            <router-link to='/start'>START</router-link>
        </button>
        
        <add-question></add-question>

        
        
        

    </div>
</template>

<script>

import AddQuestion from '@/components/AddQuestion.vue'

    export default {
  
  components: { AddQuestion },
        name: 'home-page'
    }
</script>

<style scoped>
div {
    display: grid;
}
a {
    text-decoration: none;
}

</style>