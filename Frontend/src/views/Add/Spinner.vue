<template>
    <div class="text-center">
        <b-spinner variant="success" label="Spinning" style="width: 15rem; height: 15rem;margin-top:100px;"></b-spinner>
        <h1 style="display: block;text-align:center">Trwa generacja planu...</h1>
        <h1 style="display: block;text-align:center">Może to potrwać kilka minut.</h1>
    </div>
</template>

<script>
import { BSpinner } from 'bootstrap-vue'
import Vue from 'vue'
import router from '../../router/index.js'
Vue.component('b-spinner', BSpinner)
export default {
  name: 'Spinner',
  created(){
   setTimeout(() =>  router.push("/my/school"), 60000);
  },
}
</script>
