<template>
  <div id="app">
    <img src="@/assets/logo.png"/>
    <h1 class="title">{{text.data}}</h1>
    <h1>{{text}}</h1>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  data() {
    return {
      text: ''
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:5000/')
      .then((response) => {
        this.text = response
      })
      .catch((error) => {
        this.text = error
      })
  }
})
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
