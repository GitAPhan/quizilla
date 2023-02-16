import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

const vuetify = new Vuetify({
    theme: {
        dark: true,
        themes: {
            dark: {
                primary: '#00dcc3',
                text: '#f7f7f7',
                accent: '#450303',
                secondary: '#717070',
                anchor: '#d6cfcf',
                background: "#1f1f1f"
            },
            light: {
                primary: '#d6cfcf',
                text: '#1f1f1f',
                accent: '#450303',
                secondary: '#a59e9e',
                anchor: '#464545',
                background: "#f7f7f7"
            }
        },
    },
})

export default vuetify
