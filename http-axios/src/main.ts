import Vue from 'vue'
import VueRecord from '@codekraft-studio/vue-record'
import App from './App.vue'

Vue.use(VueRecord)

Vue.config.productionTip = false

new Vue({
  render: (h) => h(App),
}).$mount('#app')
