<template>
    <div>
        <h1 ref="question_box">{{ques}}, {{totalques2}}</h1>
        <!-- <button @click="checkanswer"><p>{{ans1}}</p></button> -->
        <article v-for="(ans, index) in allans" :key="index">
            <!-- <article ref="highlightb" @click="checkanswer(ans)"> -->
            <article v-if="ans.length > 1">
            <button ref="highlightb" @click="checkanswer(ans, index)">{{ans.slice(1)}}</button>
            </article>
            </article>
        
        <!-- <button @click="checkanswer">{{ans2}}</button>
        <button @click="checkanswer">{{ans3}}</button>
        <button @click="checkanswer">{{ans4}}</button> -->
        <!-- <button @click="nextQuestion()">Next</button> -->
        <!-- <article @click="render()"> -->
        <button @click="getQuesById(cur1[count])">new question</button>
        <!-- </article> -->
        <h2>{{this.cur1}}</h2>
        <question-count></question-count>
        

    </div>
</template>

<script>
import axios from "axios"
import QuestionCount from './QuestionCount.vue'
import Cookies from "vue-cookies"


    export default {
        mounted () {
            axios.request({
                url: `http://127.0.0.1:5000/api/client`,
                method: `POST`,
                data: {
                    'id': this.cur1[0]
                }
        }).then((success)=>{
            success;
            console.log(success)
            let tempans = success.data[0].answers;
            // for(let i=0;i<success.data.length; i++) {
            // vm.$set('totalques2', success.data[0].question)
            this.totalques2 = success.data[0].question;
            this.allans = tempans.filter(word => word.length > 2);
            this.idkey = success.data[0].id
            console.log(tempans);
            this.count += 1;
            // this.$router.go(0)
            // }
            
        }).catch((error)=>{
            error
        });
        },
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
            checkanswer(ans, index) {
                if(ans.charAt(0) === "1") {
                    this.$refs[`highlightb`][index].style.backgroundColor = "green"
                    // let $ref = this.$refs[`highlightb`]
                    // $ref.style.backgroundColor = "green";
                    this.score += 1;
                    console.log('correct, green', this.$refs[`highlightb`])
                    // setTimeout(this.getQuesById(this.count), 5000);
                }
            },
   
            getQuesById(count) {
           

                axios.request({
                url: `http://127.0.0.1:5000/api/client`,
                method: `POST`,
                data: {
                    'id': count
                }
        }).then((success)=>{
            let $ref = this.$refs[`highlightb`]; 
            console.log(this.allans)
            
            if($ref[0]){
            $ref[0].style.backgroundColor = "white";
            }
            if($ref[1]){
            $ref[1].style.backgroundColor = "white";
            }
            if($ref[2]){
                $ref[2].style.backgroundColor = "white";
            }
            if($ref[3]){
                $ref[3].style.backgroundColor = "white";
            }
            
            success;
            console.log(success)
            let tempans = success.data[0].answers;
            // for(let i=0;i<success.data.length; i++) {
            // vm.$set('totalques2', success.data[0].question)
            this.totalques2 = success.data[0].question;
            this.allans = tempans.filter(word => word.length > 1);
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
    // this.$refs[highlightb] {
    //     background: red
    // }
</style>