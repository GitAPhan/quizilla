<template>
    <div>

        <img src="@/assets/godzilla.png" alt="some lizard" />
        <div class="btn-container"> 
            <button>
                <router-link to='/start'>START</router-link>
            </button>
    
            <start-game class="btn"></start-game>
            <add-question class="btn"></add-question>
        </div>

    </div>
</template>

<script>

import AddQuestion from '@/components/AddQuestion.vue'

    export default {
  
  components: { AddQuestion },
        name: 'home-page'
    }
</script>

<style lang="scss">
.home-page-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

div {
    display: grid;
}
a {
    text-decoration: none;
}

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