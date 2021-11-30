<template>
  <div>
    <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Rozpocznij dodawanie danych">

<table class="table table-striped" v-for="m in 2" :key="m">
  <thead>
    <tr>
      <th>#</th>
      <th>Poniedziałek</th>
      <th>Wtorek</th>
      <th>Środa</th>
      <th>Czwartek</th>
      <th>Piątek</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="n in 5" :key="n">
       <th scope="row">{{n}}</th>  
       <td v-for="(pp,ii) in plan" :key="ii">{{pp[n-1][m-1][1]}}</td>
    </tr>
    
   </tbody>
</table>
  </div>
</template>

<script>
import router from '../router/index.js'
export default {
  name: 'MySchool',
  data: function() {
    return { 
  plan:[[[["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]],
  [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]],
  [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]],
  [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]],
  [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]],
  [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "matematyka", ["Marcjanna Milik", ""]]]],

  [[["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "fizyka", ["Paulina Paulinowska", "308"]]],
    [["IB", "matematyka", ["Marek Markowski", ""]], ["IA", "fizyka", ["Paulina Paulinowska", "308"]]],
    [["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "j.polski", ["Barbara Barbarowicz", ""]]],
    [["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "j.polski", ["Barbara Barbarowicz", ""]]],
    [["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "j.polski", ["Barbara Barbarowicz", ""]]],
    [["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "j.polski", ["Barbara Barbarowicz", ""]]]],

  [[["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "biologia", ["Bogdan Bogdanowicz", "200"]]],
    [["IB", "fizyka", ["Paulina Paulinowska", "308"]], ["IA", "biologia", ["Bogdan Bogdanowicz", "200"]]],
    [["IB", "j.polski", ["Zbigniew Zbigniewski", ""]], ["IA", "chemia", ["Marianna Mania", "201"]]],
    [["IB", "j.polski", ["Zbigniew Zbigniewski", ""]], ["IA", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "j.polski", ["Zbigniew Zbigniewski", ""]], ["IA", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "j.polski", ["Zbigniew Zbigniewski", ""]], ["IA", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]]],

  [[["IB", "biologia", ["Bogdan Bogdanowicz", "200"]], ["IA", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "biologia", ["Bogdan Bogdanowicz", "200"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "chemia", ["Marianna Mania", "201"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]]],

  [[["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
  [["IB", "religia", ["Ksiadz Robak", ""]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]]]] 
  }},
  methods: {
    handleSubmit() {
      router.push("/step/1")
    },
  }
}
</script>

<style scoped>
.buttonm
{
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  display: block;
  width: 50%;
  margin-left: 25%;
  margin-right: 25%;
  margin-bottom:50px;
  margin-top:50px;
}

@media screen and (max-width: 1200px) 
{
  .buttonm
  {
    width: 80%;
    margin-left: 10%;
    margin-right: 10%;
  }
}
table {
  border: 1px solid black;
  margin-left:auto;
  margin-right: auto;
  width:50%
}
</style>