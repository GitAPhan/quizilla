<template>
    <div>
        <h1 ref="question_box">{{ques}}, {{totalques2}}</h1>
        <!-- <button @click="checkanswer"><p>{{ans1}}</p></button> -->
        <article v-for="(ans, index) in allans" :key="index">
            <article @click="checkanswer(ans)">
            <article v-if="ans.length > 1">
            <button ref="highlightb">{{ans.slice(1)}}</button>
            </article>
            </article>
        </article>
        <!-- <button @click="checkanswer">{{ans2}}</button>
        <button @click="checkanswer">{{ans3}}</button>
        <button @click="checkanswer">{{ans4}}</button> -->
        <button @click="nextQuestion()">Next</button>
        <article @click="render()">
        <button @click="getQuesById(cur1[count])">new question</button>
        </article>
        <question-count></question-count>
        

    </div>
</template>

<script>
import axios from "axios"
import QuestionCount from './QuestionCount.vue'
import Cookies from "vue-cookies"


    export default {
        data() {
            return {
                
                ques: "the question",
                ans1: "testing ans1",
                ans2: "testing ans2",
                ans3: "testing ans3",
                ans4: "testing ans4",
                score: 0,
                idkey: "",
                allans: [1,2,3,],
                count: 0,
                totalques2: "",
                cur1: Cookies.get('totalques'),
                highlights: "none"
                
            }
        },
  components: { QuestionCount },
        methods: {
            checkanswer(ans) {
                if(ans.charAt(0) === "1") {
                    this.$refs[`highlightb`].backgroundcolor = "green";
                    this.score += 1;
                }
            },
            // nextQuestion() {
            //     let before = [];
            //     let cur = 0;
                
            //     before = JSON.parse(Cookies.get())at
            //     cur = before.pop();
            //     Cookies.set('totalques', before);
            //     return cur

            // },
            getQuesById(count) {
                // const totalques = JSON.parse(Cookies.get('totalques'))
                // const nextQuesId = totalques.pop()
                // Cookies.set('totalques', totalques)

                axios.request({
                url: `http://127.0.0.1:5000/api/client`,
                method: `POST`,
                data: {
                    'id': count
                }
        }).then((success)=>{
            success;
            console.log(success)
            // for(let i=0;i<success.data.length; i++) {
            // vm.$set('totalques2', success.data[0].question)
            this.totalques2 = success.data[0].question;
            this.allans = success.data[0].answers;
            this.idkey = success.data[0].id
            this.count += 1;
            // this.$router.go(0)
            // }
            
        }).catch((error)=>{
            error
        })
        },
        },
    
    
        
   
        name: "quiz-screen"
    }
</script>

<style lang="scss" scoped>
    div {
        display: grid;
        grid-row: auto;
        place-content: center;
    }
    button {
        max-width: 70vh;
    }
    highlightbutton {}
</style>