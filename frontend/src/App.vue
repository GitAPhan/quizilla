<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <router-link
          to="/"
        ><v-img 
          alt="Quizilla Logo" 
            class="shrink mr-2" 
            contain
            src="@/assets/godzilla.png"
            transition="scale-transition" 
            width="40" 
        /></router-link>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    cssProps() {
      var themeColors = {};
      var theme = "light";
      if (this.$vuetify.theme.isDark) {
        theme = "dark";
      }
      Object.keys(this.$vuetify.theme.themes[theme]).forEach((color) => {
        themeColors[`--v-${color}`] = this.$vuetify.theme.themes[theme][color];
      });
      return themeColors;
    },
  },
  data: () => ({
    //
  }),
};
</script>
