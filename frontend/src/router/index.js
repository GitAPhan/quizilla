import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import StartGame from '@/views/StartGame.vue'
import AddQuestionPage from '@/views/AddQuestionPage'



Vue.use(VueRouter)

const routes = [
  {
  path: '/',
  component: HomePage
},
{
  path: '/start',
  component: StartGame
},
{
  path: '/add-question',
  component: AddQuestionPage
}
]

const router = new VueRouter({
  routes
})

export default router
