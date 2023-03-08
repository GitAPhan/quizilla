<template>
  <div>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-container class="pa-15">
        <v-row>
          <v-text-field
            v-model="question"
            :rules="questionRules"
            :counter="255"
            label="Question"
            required
          ></v-text-field>
        </v-row>
        <v-radio-group v-model="ans_cor">
          <v-row v-for="n in ans_qty" :key="n">
            <v-radio :value="n"></v-radio>
            <v-text-field
              :v-model="`ans_${n}`"
              :rules="answerRules"
              :counter="150"
              :label="ans_cor === n ? 'correct answer' : 'answer'"
              required
            ></v-text-field>
          </v-row>
        </v-radio-group>
        <v-checkbox
          v-model="checkbox"
          :rules="(v) => !!v || 'you must agree to continue'"
          label="by checking this box you have confirmed that you are not a dick and your submission is valid"
          required
        ></v-checkbox>
        <v-btn :disabled="!checkbox">Submit</v-btn>
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
    ans_qty: 4, //maybe use to add/subtract amount of answers
    ans_1: "",
    ans_2: "",
    ans_3: "",
    ans_4: "",
    ans_cor: "",
    checkbox: false,
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
    answerRules: [
      (value) => {
        if (value) return true;

        return "Answer is required.";
      },
      (value) => {
        if (value?.length <= 150) return true;

        return "Answer must be less than 150 characters.";
      },
    ],
    answerRulesOption: [
      (value) => {
        if (value?.length <= 150) return true;

        return "Answer must be less than 150 characters.";
      },
    ],
  }),
};
</script>

<style lang="sass" scoped>
</style>