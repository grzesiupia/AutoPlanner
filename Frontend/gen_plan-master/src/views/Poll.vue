<template>
  <div>
    <table class="table table-striped">
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
    <tr v-for="(p,i) in poll[0]" :key="i">
       <th scope="row">{{ p.Hour  }}</th>  
       <td><input type="checkbox" id="checkbox" v-model="p.Selected"></td>   
       <td><input type="checkbox" id="checkbox" v-model="poll[1][i].Selected"></td>  
       <td><input type="checkbox" id="checkbox" v-model="poll[2][i].Selected"></td>  
       <td><input type="checkbox" id="checkbox" v-model="poll[3][i].Selected"></td>  
       <td><input type="checkbox" id="checkbox" v-model="poll[4][i].Selected"></td>  
       
    </tr>
    
   </tbody>
       </table>
<input class=" btn btn-success mr-3" @click="submit" type="submit" value="Wyślij" >
  </div>
</template>

<script>

export default {
  name: 'Poll',
  data: function() {
    return { 
    poll: [
        [{'Day': 'Poniedziałek', 'Hour': 1, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 2, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 3, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 4, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 5, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 6, 'Selected': false}, {'Day': 'Poniedziałek', 'Hour': 7, 'Selected': false}],
            [{'Day': 'Wtorek', 'Hour': 1, 'Selected': false}, {'Day': 'Wtorek','Hour': 2, 'Selected': false}, {'Day': 'Wtorek','Hour': 3, 'Selected': false}, {'Day': 'Wtorek','Hour': 4, 'Selected': false}, {'Day': 'Wtorek','Hour': 5, 'Selected': false}, {'Day': 'Wtorek','Hour': 6, 'Selected': false}, {'Day': 'Wtorek','Hour': 7, 'Selected': false}],
            [{'Day': 'Środa', 'Hour': 1, 'Selected': false}, {'Day':'Środa','Hour': 2, 'Selected': false}, {'Day':'Środa','Hour': 3, 'Selected': false}, {'Day':'Środa','Hour': 4, 'Selected': false}, {'Day':'Środa','Hour': 5, 'Selected': false}, {'Day':'Środa','Hour': 6, 'Selected': false}, {'Day':'Środa','Hour': 7, 'Selected': false}],
            [{'Day': 'Czwartek', 'Hour': 1, 'Selected': false}, {'Day':'Czwartek' , 'Hour': 2, 'Selected': false},{'Day':'Czwartek' , 'Hour': 3, 'Selected': false},{'Day':'Czwartek' , 'Hour': 4, 'Selected': false},{'Day':'Czwartek' , 'Hour': 5, 'Selected': false},{'Day':'Czwartek' , 'Hour': 6, 'Selected': false},{'Day':'Czwartek' , 'Hour': 7, 'Selected': false}],
            [{'Day': 'Piątek', 'Hour': 1, 'Selected': false}, {'Day':'Piątek', 'Hour': 2, 'Selected': false},{'Day':'Piątek', 'Hour': 3, 'Selected': false},{'Day':'Piątek', 'Hour': 4, 'Selected': false},{'Day':'Piątek', 'Hour': 5, 'Selected': false},{'Day':'Piątek', 'Hour': 6, 'Selected': false},{'Day':'Piątek', 'Hour': 7, 'Selected': false}],
    ],
  
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
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]]],

  [[["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
  [["IB", "religia", ["Ksiadz Robak", ""]]], [["IB", "religia", ["Ksiadz Robak", ""]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]],
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]]]]] 
    }
  },

  methods:
  {
  submit(e)
    {
      e.preventDefault();
       this.$store.dispatch(
        "sendPoll",
        {
          poll:this.poll
        }
      )
    }
  }
}
</script>
<style scoped>
input[type=checkbox]
{
  /* Double-sized Checkboxes */
  -ms-transform: scale(3); /* IE */
  -moz-transform: scale(3); /* FF */
  -webkit-transform: scale(3); /* Safari and Chrome */
  -o-transform: scale(3); /* Opera */
  transform: scale(3);
  padding: 10px;
}
table {
  border: 1px solid black;
  margin-left:auto;
  margin-right: auto;
  width:50%
}
</style>
