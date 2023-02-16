<template>
  <div>
    <img src="@/assets/godzilla.png" alt="some lizard" />
    <button>
      <router-link to="/start">START</router-link>
    </button>

    <button><router-link to="/add-question">ADD QUESTION</router-link></button
    >
  </div>
</template>

<script>

export default {
  name: "home-page",
};
</script>

<style scoped>
div {
  display: grid;
}
a {
  text-decoration: none;
}
</style>