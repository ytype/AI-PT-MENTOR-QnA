<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <vue-record-audio @result="onResult" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  methods: {
    fetchData() {
      axios.get('localhost:5000')
        .then((response) => {
          console.log(response)
        })
    },
    onResult(data: any) {
      console.log('The blob data:', data)
      console.log('Downloadable audio', window.URL.createObjectURL(data))
    },
  },
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
