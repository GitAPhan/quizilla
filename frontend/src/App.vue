<template>
  <div id='app'>
    <nav>
      <router-link to='/'>QUIZZILLA, this is in app.vue</router-link>
      
      <!-- <img :src = "src/assets/godzilla.png"> -->
    </nav>
      <router-view/>
      
      <!-- <router-link to="/home">testing2</router-link> -->
    
  </div>
</template>

<script>

  


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
div nav a {
    text-decoration: none;
}
</style>
