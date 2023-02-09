<template>
  <div id='app'>
    <router-view></router-view>
  </div>
</template>

<script>
</script>

<style lang="scss">
$tablet: 650px;
$laptop: 1024px;

body {
  background-image: linear-gradient(#7889f3, #413a76, #071339);
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

button {
    border-radius: 25px;
    margin: 10px 10px 5px;
    padding: 7px 20px;
}

</style>
