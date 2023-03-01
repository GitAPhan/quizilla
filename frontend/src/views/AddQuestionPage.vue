<template>
  <div>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="question"
              :rules="questionRules"
              :counter="255"
              label="Question"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="lastname"
              :rules="nameRules"
              :counter="10"
              label="Last name"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "add-question-page",
  data: () => ({
    valid: false,
    question: "",
    lastname: "",
    questionRules: [
      (value) => {
        if (value) return true;

        return "Question is required.";
      },
      (value) => {
        if (value?.length <= 255) return true;

        return "Question must be less than 255 characters.";
      },
    ],
    nameRules: [
      (value) => {
        if (value) return true;

        return "Question is required.";
      },
      (value) => {
        if (value?.length <= 10) return true;

        return "Question must be less than 255 characters.";
      },
    ],
    email: "",
    emailRules: [
      (value) => {
        if (value) return true;

        return "E-mail is requred.";
      },
      (value) => {
        if (/.+@.+\..+/.test(value)) return true;

        return "E-mail must be valid.";
      },
    ],
  }),
};
</script>

<style lang="sass" scoped>
</style>