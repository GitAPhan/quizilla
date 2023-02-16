<template>
    <div>
        <h1 ref="question_box">{{ques}}, {{totalques}}</h1>
        <button @click="checkanswer">{{ans1}}</button>
        <button @click="checkanswer">{{ans2}}</button>
        <button @click="checkanswer">{{ans3}}</button>
        <button @click="checkanswer">{{ans4}}</button>
        

    </div>
</template>

<script>
import axios from "axios"


    export default {
        methods: {
            name() {
                
            }
        },
        data() {
            return {
                
                ques: "the question",
                ans1: "testing ans1",
                ans2: "testing ans2",
                ans3: "testing ans3",
                ans4: "testing ans4",
                totalques: []
                
            }
        },
        mounted () {
            axios.request({
                url: `http://127.0.0.1:5000/api/client`,
        
           
        }).then((success)=>{
            success
            console.log(success)

        
            // this.ques = "this is successful"
            // this.ques = success.data[0][`question`]
            // for(let i=0;i<success.data.length; i++) {
            //     this.totalques.push(success.data[i][`id`])
            // }
            // let selectedQuestions = [];
            // const getRandomIndex = (arr) => Math.floor(Math.random()*this.totalques.length)

            // const getRandomObject = (arr) => {
            //     const random = getRandomIndex(arr);
            //     if (selectedQuestions.includes(random)) {
            //         return getRandomObject(arr);
        
            //     }
            //     selectedQuestions.push(random);

            // }

            this.ans1 = success
            
        }).catch((error)=>{
            error
        })
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
</style>