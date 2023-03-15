<template>
    <div>
        <h1>{{new_random}}</h1>
    </div>
</template>

<script>
import axios from 'axios'
import Cookies from "vue-cookies"
import _ from 'lodash'

    export default {
        methods: {
            shuffle() {
                this.new_random = _.shuffle(this.totalques)
            }
        },
        data() {
            return {
                totalques: [],
                new_random: []
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
            for(let i=0;i<success.data.length; i++) {
                this.totalques.push(success.data[i][`id`])
            
            this.shuffle()
            
            Cookies.set('totalques', JSON.stringify(this.new_random))
            // }
            // let selectedQuestions = [];
            // const getRandomIndex = (arr) => Math.floor(Math.random()*this.totalques.length)

            // const getRandomObject = (arr) => {
            //     const random = getRandomIndex(arr);
            //     if (selectedQuestions.includes(random)) {
            //         return getRandomObject(arr);
        
            //     }
            //     selectedQuestions.push(random);

            }

            this.ans1 = success
            
        }).catch((error)=>{
            error
        })
        },
        name: 'question-count'
    }
</script>

<style lang="scss" scoped>

</style>