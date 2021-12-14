<template>
  <div>
    <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Rozpocznij dodawanie danych">
    <p><input class="buttonk btn btn-success mr-3" type="submit" @click="planClass" value="Plany dla klas">
    <input class="buttonk btn btn-success mr-3" type="submit" @click="planTeacher" value="Plany dla nauczycieli">
    <input class="buttonk btn btn-success mr-3" type="submit" @click="planClassroom" value="Plany dla sal">
    </p>
<div v-if="this.selectedPlans==='class'">
<table class="table table-striped" v-for="(m,ii) in this.classes" :key="ii" >
  <thead>
    <tr>
      <th>{{m.name}}</th>
      <th>Poniedziałek</th>
      <th>Wtorek</th>
      <th>Środa</th>
      <th>Czwartek</th>
      <th>Piątek</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="n in plan2[0].length" :key="n">
       <th scope="row">{{n}}</th>  
       <td v-for="(p,i) in plan2" :key="i"><div v-if="plan2[i][n-1] && m.name in plan2[i][n-1]">{{plan2[i][n-1][m.name][0]}}</div><div v-else></div></td>
    </tr>
   </tbody>
</table>
</div>
  </div>
</template>

<script>
import router from '../router/index.js'
export default {
  name: 'MySchool',
  computed: {
    classPlans(){
      return this.$store.getters.getClassPlans;
    },
    teacherPlans(){
      return this.$store.getters.getTeacherPlans;
    },
    classroomPlans(){
      return this.$store.getters.getClassroomPlans;
    },
    token() 
    {
      return this.$store.getters.getToken;
    },
    classes(){
      return this.$store.getters.getClasses;
    },
  },
  created(){
    this.$store.dispatch("fetchClassPlans",{ token:this.token});
    this.$store.dispatch("fetchTeacherPlans",{ token:this.token});
    this.$store.dispatch("fetchClassroomPlans",{ token:this.token});
    this.$store.dispatch("fetchClasses",{ token:this.token});
  },
  data: function() {
    return { 
  selectedPlans:"class",
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
    [["IB", "wf", ["Wlodzimierz Wlodzimski", "Sala gimnastyczna"]], ["IA", "religia", ["Ksiadz Robak", ""]]]]],
  plan2:[[{'1b': ['historia', 'HV', 15], '3f': ['j.angielski', 'EZ', 213], '3b': ['j.angielski', 'EP', 206], '1g': ['geografia', 'ŁS', 103], '1a': ['j.polski', 'RS', 106], '2a': ['wf', 'HR', 's1'], '3a': ['j.polski', 'MJ', 203], '3e': ['j.niemiecki', 'GW', 109], '2b': ['historia', 'HW', 107], '1c': ['chemia', 'MC', 115], '2c': ['j.niemiecki', 'MU', 316], '2g': ['matematyka', 'AR', 7], '3d': ['j.polski', 'AM', 108], '1e': ['informatyka', 'KI', 216], '1d': ['informatyka', 'IW', 304], '2e': ['j.niemiecki', 'ER', 208], '1f': ['matematyka', 'BP', 105], '2d': ['wf', 'BD', 's2'], '3c': ['j.angielski', 'BH', 205]},
{'2c': ['j.polski', 'PS', 15], '3a': ['chemia', 'Ma', 213], '2g': ['wf', 'HR', 's1'], '3d': ['wos', 'AS', 206], '2a': ['historia', 'PE', 103], '3f': ['geografia', 'CK', 106], '2b': ['j.polski', 'RS', 203], '3e': ['matematyka', 'MV', 109], '1a': ['wf', 'BD', 's2'], '1d': ['j.niemiecki', 'GW', 107], '2e': ['wf', 'IR', 's3'], '1c': ['fizyka', 'MB', 115], '1f': ['edb', 'LF', 316], '1e': ['religia', 'GP', 7], '3c': ['biologia', 'Wa', 108], '1b': ['matematyka', 'MR', 216], '1g': ['geografia', 'ŁS', 304], '3b': ['j.hiszpański', 'RO', 208], '2d': ['biologia', 'Sm', 105]},
{'3a': ['religia', 'WK', 15], '2c': ['wf', 'KS', 's1'], '2b': ['j.polski', 'RS', 213], '2g': ['geografia', 'ŁS', 206], '3c': ['biologia', 'Wa', 103], '1a': ['edb', 'LF', 106], '1d': ['chemia', 'DW', 203], '3d': ['j.polski', 'AM', 109], '3b': ['geografia', 'CK', 107], '2e': ['historia', 'VR', 115], '1b': ['informatyka', 'IW', 316], '3f': ['wf', 'MM', 's2'], '1g': ['wf', 'IR', 's3'], '1e': ['fizyka', 'MB', 7], '1f': ['j.angielski', 'AB', 108], '1c': ['j.niemiecki', 'MU', 216], '3e': ['j.niemiecki', 'GW', 304], '2d': ['historia', 'PE', 208], '2a': ['biologia', 'JW', 105]},
{'2c': ['chemia', 'MC', 15], '3c': ['j.niemiecki', 'MW', 213], '2g': ['chemia', 'DW', 206], '2b': ['religia', 'GP', 103], '3d': ['j.polski', 'AM', 106], '1d': ['historia', 'HW', 203], '1b': ['matematyka', 'MR', 109], '1e': ['j.polski', 'MK', 107], '1a': ['fizyka', 'MB', 115], '1g': ['wf', 'IR', 's1'], '1c': ['biologia', 'Wa', 316], '3a': ['matematyka', 'KT', 7], '3e': ['j.angielski', 'JK', 108], '2d': ['wos', 'VR', 216], '3b': ['religia', 'WK', 304], '2e': ['geografia', 'ŁS', 208], '1f': ['wf', 'BD', 's2'], '2a': ['j.niemiecki', 'MU', 105], '3f': ['j.angielski', 'EZ', 205]},
{'1g': ['biologia', 'Sm', 15], '2b': ['wf', 'MM', 's1'], '1d': ['j.polski', 'PS', 213], '2e': ['wos', 'BC', 206], '1e': ['j.angielski', 'JK', 103], '2d': ['geografia', 'Wg', 106], '3c': ['j.niemiecki', 'MW', 203], '2c': ['chemia', 'MC', 109], '2g': ['matematyka', 'AR', 107], '3d': ['historia', 'VR', 115], '1c': ['j.łac', 'Sz', 316], '3f': ['j.polski', 'MJ', 7], '3b': ['matematyka', 'KT', 108], '3e': ['wf', 'HR', 's2'], '2a': ['j.niemiecki', 'MU', 216], '3a': ['j.angielski', 'KJ', 304], '1a': ['matematyka', 'BP', 208], '1f': ['j.niemiecki', 'ER', 105], '1b': ['edb', 'LF', 205]},
{'1d': ['j.angielski', 'RP', 15], '2d': ['pp', 'BC', 213], '2c': ['fizyka', 'ŁS', 206], '2b': ['zaj.art', 'RS', 103], '2g': ['religia', 'GP', 106], '2a': ['biologia', 'JW', 203], '2e': ['informatyka', 'DD', 109], '1c': ['matematyka', 'BP', 107], '1g': ['j.rosyjski', 'ER', 115], '1e': ['j.polski', 'MK', 316], '3a': ['j.polski', 'MJ', 7], '3c': ['biologia', 'Wa', 108], '3d': ['wf', 'IR', 's1'], '1f': ['wos', 'EP', 216], '1a': ['j.niemiecki', 'MU', 304], '3f': ['geografia', 'CK', 208], '1b': ['geografia', 'Wg', 105], '3e': ['matematyka', 'MV', 205], '3b': ['historia', 'PE', 23]},
{'2e': ['fizyka', 'ŁS', 15], '2c': ['matematyka', 'MR', 213], '2d': ['j.angielski', 'BH', 206], '2a': ['chemia', 'Ma', 103], '2b': ['informatyka', 'KI', 106], '1g': ['edb', 'LF', 203], '1f': ['biologia', 'JW', 109], '1c': ['wf', 'HR', 's1'], '1a': ['religia', 'GP', 107], '2g': ['biologia', 'Sm', 115], '1b': ['historia', 'HV', 316], '1e': ['wos', 'AS', 7]},
{'2e': ['j.polski', 'AM', 15], '2b': ['biologia', 'Sm', 213], '2a': ['informatyka', 'IW', 206]}],

[{'1b': ['biologia', 'Sm', 15], '2a': ['chemia', 'Ma', 213], '3f': ['geografia', 'CK', 206], '2b': ['wf', 'MM', 's1'], '1c': ['wf', 'HR', 's2'], '1a': ['chemia', 'DW', 103], '1d': ['historia', 'HW', 106], '3a': ['matematyka', 'KT', 203], '1g': ['matematyka', 'MV', 109], '2c': ['j.angielski', 'AB', 107], '2g': ['j.polski', 'PS', 115], '1f': ['wf', 'BD', 's3'], '3d': ['historia', 'VR', 316], '3b': ['historia', 'PE', 7], '1e': ['matematyka', 'MR', 108], '3c': ['chemia', 'MC', 216], '2e': ['j.niemiecki', 'ER', 304], '2d': ['j.niemiecki', 'GW', 208], '3e': ['fizyka', 'MB', 105]},
{'3a': ['j.angielski', 'KJ', 15], '3e': ['wf', 'HR', 's1'], '2c': ['historia', 'VR', 213], '2b': ['chemia', 'Ma', 206], '1a': ['j.polski', 'RS', 103], '3b': ['historia', 'PE', 106], '1d': ['j.polski', 'PS', 203], '2g': ['j.angielski', 'BH', 109], '1f': ['wf', 'BD', 's2'], '2a': ['j.polski', 'AM', 107], '2e': ['chemia', 'DW', 115], '3f': ['j.angielski', 'EZ', 316], '1c': ['j.angielski', 'RR', 7], '3c': ['chemia', 'MC', 108], '1b': ['j.łac', 'Sz', 216], '1e': ['matematyka', 'MR', 304], '3d': ['przyroda', 'Sm', 208], '1g': ['matematyka', 'MV', 105], '2d': ['j.polski', 'MK', 205]},
{'3a': ['biologia', 'JW', 15], '2c': ['matematyka', 'MR', 213], '2b': ['chemia', 'Ma', 206], '1d': ['j.polski', 'PS', 103], '3c': ['matematyka', 'AR', 106], '2a': ['j.polski', 'AM', 203], '2g': ['geografia', 'ŁS', 109], '1a': ['chemia', 'DW', 107], '2e': ['religia', 'WK', 115], '1b': ['j.polski', 'MK', 316], '3b': ['j.polski', 'MJ', 7], '1g': ['religia', 'GP', 108], '1e': ['wf', 'KS', 's1'], '3f': ['j.angielski', 'EZ', 216], '3e': ['matematyka', 'MV', 304], '1c': ['j.angielski', 'RR', 208], '3d': ['wos', 'AS', 105], '2d': ['wf', 'BD', 's2'], '1f': ['j.angielski', 'AB', 205]},
{'2g': ['chemia', 'DW', 15], '2b': ['wos', 'BC', 213], '2c': ['wf', 'KS', 's1'], '1g': ['historia', 'HW', 206], '1e': ['j.angielski', 'JK', 103], '1d': ['j.polski', 'PS', 106], '1c': ['religia', 'GP', 203], '3d': ['matematyka', 'KT', 109], '2d': ['matematyka', 'AR', 107], '3a': ['biologia', 'JW', 115], '3c': ['j.polski', 'MJ', 316], '3e': ['matematyka', 'MV', 7], '2e': ['j.angielski', 'RO', 108], '1a': ['wf', 'BD', 's2'], '3b': ['geografia', 'CK', 216], '1b': ['religia', 'WK', 304], '2a': ['matematyka', 'BP', 208], '1f': ['j.polski', 'RS', 105], '3f': ['matematyka', 'AT', 205]},
{'2b': ['religia', 'GP', 15], '1g': ['matematyka', 'MV', 213], '2e': ['j.polski', 'AM', 206], '1d': ['j.polski', 'PS', 103], '1e': ['j.łac', 'Sz', 106], '2g': ['pp', 'BC', 203], '2d': ['informatyka', 'IW', 109], '2c': ['chemia', 'MC', 107], '3d': ['j.niemiecki', 'KJ', 115], '1c': ['geografia', 'Wg', 316], '3c': ['historia', 'VR', 7], '3a': ['wf', 'MM', 's1'], '2a': ['biologia', 'JW', 108], '3e': ['j.angielski', 'JK', 216], '3b': ['matematyka', 'KT', 304], '3f': ['j.polski', 'MJ', 208], '1a': ['wf', 'BD', 's2'], '1f': ['matematyka', 'BP', 105], '1b': ['j.angielski', 'RP', 205]},
{'2b': ['matematyka', 'AT', 15], '2d': ['chemia', 'DW', 213], '1g': ['geografia', 'ŁS', 206], '2c': ['j.angielski', 'AB', 103], '2a': ['biologia', 'JW', 106], '1d': ['matematyka', 'MV', 203], '2g': ['j.polski', 'PS', 109], '1f': ['j.polski', 'RS', 107], '2e': ['j.angielski', 'RO', 115], '3a': ['j.polski', 'MJ', 316], '1e': ['biologia', 'Sm', 7], '3e': ['religia', 'GP', 108], '1b': ['j.polski', 'MK', 216], '3d': ['matematyka', 'KT', 304], '3c': ['biologia', 'Wa', 208], '1c': ['wos', 'AS', 105], '3b': ['geografia', 'CK', 205], '1a': ['j.łac', 'Sz', 23], '3f': ['historia', 'VR', 209]},
{'2e': ['pp', 'BC', 15], '2g': ['geografia', 'ŁS', 213], '2d': ['j.niemiecki', 'GW', 206], '2a': ['religia', 'WK', 103], '2c': ['geografia', 'CK', 106], '2b': ['j.angielski', 'EP', 203], '1d': ['edb', 'LF', 109]},
{}],

[{'2a': ['wos', 'BC', 15], '3a': ['chemia', 'Ma', 213], '2b': ['j.niemiecki', 'KJ', 206], '1b': ['fizyka', 'MB', 103], '3f': ['matematyka', 'AT', 106], '3e': ['matematyka', 'MV', 203], '1a': ['biologia', 'JW', 109], '2g': ['wf', 'HR', 's1'], '1d': ['wos', 'AS', 107], '2c': ['historia', 'VR', 115], '1c': ['biologia', 'Wa', 316], '1e': ['j.polski', 'MK', 7], '3c': ['chemia', 'MC', 108], '2e': ['matematyka', 'KT', 216], '1f': ['religia', 'WK', 304], '3b': ['j.polski', 'MJ', 208], '2d': ['biologia', 'Sm', 105], '3d': ['j.polski', 'AM', 205], '1g': ['historia', 'HW', 23]},
{'2c': ['j.angielski', 'AB', 15], '3a': ['biologia', 'JW', 213], '2a': ['chemia', 'Ma', 206], '2b': ['matematyka', 'AT', 103], '1d': ['fizyka', 'MB', 106], '3b': ['historia', 'PE', 203], '1a': ['religia', 'GP', 109], '3d': ['j.polski', 'AM', 107], '2e': ['informatyka', 'DD', 115], '3e': ['matematyka', 'MV', 316], '2g': ['wf', 'HR', 's1'], '3f': ['j.angielski', 'EZ', 7], '1f': ['j.polski', 'RS', 108], '3c': ['chemia', 'MC', 216], '1c': ['j.angielski', 'RR', 304], '1b': ['chemia', 'DW', 208], '1e': ['matematyka', 'MR', 105], '1g': ['j.łac', 'Sz', 205], '2d': ['j.polski', 'MK', 23]},
{'3a': ['historia', 'HV', 15], '2c': ['chemia', 'MC', 213], '3c': ['matematyka', 'AR', 206], '1g': ['j.polski', 'AM', 103], '2b': ['j.angielski', 'EP', 106], '2g': ['religia', 'GP', 203], '1d': ['wf', 'MM', 's1'], '1e': ['fizyka', 'MB', 109], '2e': ['matematyka', 'KT', 107], '1a': ['biologia', 'JW', 115], '3f': ['j.polski', 'MJ', 316], '1b': ['wos', 'AS', 7], '2d': ['chemia', 'DW', 108], '1c': ['j.polski', 'RS', 216], '3d': ['religia', 'WK', 304], '3b': ['wos', 'BC', 208], '3e': ['j.polski', 'PS', 105], '2a': ['j.angielski', 'RO', 205], '1f': ['geografia', 'Wg', 23]},
{'2g': ['j.angielski', 'BH', 15], '2c': ['j.polski', 'PS', 213], '2b': ['geografia', 'Wg', 206], '2e': ['chemia', 'DW', 103], '1a': ['historia', 'HW', 106], '1g': ['informatyka', 'IW', 203], '2d': ['wf', 'BD', 's1'], '3d': ['j.angielski', 'AB', 109], '3e': ['j.angielski', 'JK', 107], '1d': ['matematyka', 'MV', 115], '3a': ['chemia', 'Ma', 316], '1c': ['j.niemiecki', 'MU', 7], '3c': ['biologia', 'Wa', 108], '1e': ['historia', 'HV', 216], '3b': ['wf', 'KS', 's2'], '3f': ['religia', 'WK', 304], '1b': ['j.polski', 'MK', 208], '1f': ['fizyka', 'ŁS', 105], '2a': ['historia', 'PE', 205]},
{'1g': ['j.rosyjski', 'ER', 15], '2b': ['pp', 'BC', 213], '1d': ['biologia', 'Sm', 206], '2d': ['religia', 'GP', 103], '2c': ['j.polski', 'PS', 106], '1e': ['wf', 'KS', 's1'], '2g': ['matematyka', 'AR', 203], '1c': ['historia', 'HW', 109], '1f': ['geografia', 'Wg', 107], '2a': ['matematyka', 'BP', 115], '3d': ['j.angielski', 'AB', 316], '2e': ['geografia', 'ŁS', 7], '3f': ['historia', 'VR', 108], '3e': ['j.niemiecki', 'GW', 216], '3c': ['chemia', 'MC', 304], '3a': ['biologia', 'JW', 208], '1b': ['j.polski', 'MK', 105], '1a': ['j.polski', 'RS', 205], '3b': ['geografia', 'CK', 23]},
{'2b': ['j.polski', 'RS', 15], '2d': ['fizyka', 'ŁS', 213], '1d': ['j.angielski', 'RP', 206], '2a': ['chemia', 'Ma', 103], '2g': ['j.rosyjski', 'ER', 106], '2c': ['pp', 'BC', 203], '2e': ['matematyka', 'KT', 109], '1g': ['matematyka', 'MV', 107], '3a': ['j.niemiecki', 'MW', 115], '1f': ['matematyka', 'BP', 316], '3d': ['j.angielski', 'AB', 7], '1b': ['j.polski', 'MK', 108], '1e': ['wf', 'KS', 's1'], '3f': ['matematyka', 'AT', 216], '3c': ['j.polski', 'MJ', 304], '1c': ['chemia', 'MC', 208], '1a': ['j.niemiecki', 'MU', 105], '3e': ['historia', 'HV', 205]},
{'2e': ['wf', 'IR', 's1'], '2d': ['historia', 'PE', 15], '2c': ['chemia', 'MC', 213], '2g': ['j.angielski', 'BH', 206], '2b': ['biologia', 'Sm', 103], '2a': ['j.angielski', 'RO', 106]},
{}],

[{'2a': ['historia', 'PE', 15], '2b': ['j.polski', 'RS', 213], '3f': ['matematyka', 'AT', 206], '3e': ['j.polski', 'PS', 103], '1b': ['j.niemiecki', 'MW', 106], '3a': ['wf', 'MM', 's1'], '2e': ['historia', 'VR', 203], '2c': ['geografia', 'CK', 109], '1a': ['j.angielski', 'RR', 107], '2g': ['wos', 'BC', 115], '1c': ['edb', 'LF', 316], '1f': ['matematyka', 'BP', 7], '3d': ['matematyka', 'KT', 108], '1d': ['religia', 'WK', 216], '2d': ['matematyka', 'AR', 304], '3b': ['wf', 'KS', 's2'], '1g': ['wos', 'AS', 208], '1e': ['geografia', 'Wg', 105], '3c': ['biologia', 'Wa', 205]},
{'3a': ['matematyka', 'KT', 15], '2c': ['biologia', 'Wa', 213], '1d': ['j.niemiecki', 'GW', 206], '1a': ['j.polski', 'RS', 103], '3b': ['historia', 'PE', 106], '2b': ['historia', 'HW', 203], '2e': ['j.polski', 'AM', 109], '2g': ['matematyka', 'AR', 107], '3f': ['matematyka', 'AT', 115], '2a': ['matematyka', 'BP', 316], '1f': ['informatyka', 'DD', 7], '1b': ['j.niemiecki', 'MW', 108], '3c': ['historia', 'VR', 216], '3d': ['wf', 'IR', 's1'], '1g': ['religia', 'GP', 304], '1e': ['matematyka', 'MR', 208], '1c': ['wf', 'HR', 's2'], '3e': ['matematyka', 'MV', 105], '2d': ['j.polski', 'MK', 205]},
{'2c': ['wos', 'BC', 15], '3a': ['j.niemiecki', 'MW', 213], '2b': ['matematyka', 'AT', 206], '3c': ['religia', 'GP', 103], '2g': ['informatyka', 'IW', 106], '3d': ['j.polski', 'AM', 203], '1g': ['chemia', 'Ma', 109], '1d': ['matematyka', 'MV', 107], '1e': ['historia', 'HV', 115], '1a': ['biologia', 'JW', 316], '3f': ['geografia', 'CK', 7], '2e': ['wf', 'IR', 's1'], '1c': ['historia', 'HW', 108], '1b': ['j.polski', 'MK', 216], '3e': ['fizyka', 'MB', 304], '3b': ['j.polski', 'MJ', 208], '1f': ['j.polski', 'RS', 105], '2d': ['j.angielski', 'BH', 205], '2a': ['religia', 'WK', 23]},
{'2c': ['j.niemiecki', 'MU', 15], '2g': ['matematyka', 'AR', 213], '1g': ['fizyka', 'MB', 206], '2b': ['j.polski', 'RS', 103], '2d': ['wos', 'VR', 106], '1d': ['religia', 'WK', 203], '2e': ['j.angielski', 'RO', 109], '3d': ['j.polski', 'AM', 107], '1e': ['religia', 'GP', 115], '3c': ['j.angielski', 'BH', 316], '3a': ['j.polski', 'MJ', 7], '3e': ['j.angielski', 'JK', 108], '1c': ['chemia', 'MC', 216], '1a': ['wos', 'AS', 304], '3b': ['j.angielski', 'EP', 208], '2a': ['geografia', 'Wg', 105], '1f': ['chemia', 'DW', 205], '1b': ['wf', 'IR', 's1'], '3f': ['wf', 'MM', 's2']},
{'1g': ['j.polski', 'AM', 15], '1d': ['j.angielski', 'RP', 213], '2d': ['matematyka', 'AR', 206], '2b': ['j.polski', 'RS', 103], '2c': ['biologia', 'Wa', 106], '1e': ['edb', 'LF', 203], '2g': ['historia', 'PE', 109], '2e': ['biologia', 'Sm', 107], '2a': ['j.angielski', 'RO', 115], '1c': ['informatyka', 'KI', 316], '1a': ['geografia', 'Wg', 7], '1f': ['j.łac', 'Sz', 108], '3b': ['wos', 'BC', 216], '3c': ['wf', 'BD', 's1'], '3e': ['wf', 'HR', 's2'], '1b': ['matematyka', 'MR', 304], '3a': ['biologia', 'JW', 208], '3f': ['j.polski', 'MJ', 105], '3d': ['historia', 'VR', 205]},
{'2d': ['matematyka', 'AR', 15], '2b': ['matematyka', 'AT', 213], '2e': ['fizyka', 'ŁS', 206], '2a': ['historia', 'PE', 103], '2c': ['religia', 'WK', 106], '2g': ['j.polski', 'PS', 203], '1g': ['j.angielski', 'RR', 109], '1c': ['j.polski', 'RS', 107], '1e': ['chemia', 'Ma', 115], '1f': ['j.angielski', 'AB', 316], '3a': ['biologia', 'JW', 7], '1d': ['wos', 'AS', 108], '3d': ['przyroda', 'Sm', 216], '1b': ['historia', 'HV', 304], '1a': ['matematyka', 'BP', 208], '3b': ['j.polski', 'MJ', 105], '3f': ['j.angielski', 'EZ', 205], '3c': ['wf', 'BD', 's1'], '3e': ['fizyka', 'MB', 23]},
{'2d': ['j.polski', 'MK', 15], '2e': ['biologia', 'Sm', 213], '2c': ['biologia', 'Wa', 206], '2b': ['geografia', 'Wg', 103], '2a': ['wf', 'HR', 's1'], '2g': ['j.polski', 'PS', 106]},
{}],

[{'2b': ['j.niemiecki', 'KJ', 15], '3e': ['j.polski', 'PS', 213], '3f': ['matematyka', 'AT', 206], '2a': ['historia', 'PE', 103], '3d': ['historia', 'VR', 106], '3a': ['historia', 'HV', 203], '2g': ['biologia', 'Sm', 109], '1a': ['chemia', 'DW', 107], '2c': ['wf', 'KS', 's1'], '1d': ['wf', 'MM', 's2'], '2e': ['matematyka', 'KT', 115], '1c': ['religia', 'GP', 316], '1f': ['matematyka', 'BP', 7], '2d': ['geografia', 'Wg', 108], '1b': ['j.angielski', 'RP', 216], '1e': ['j.angielski', 'JK', 304], '3c': ['wf', 'BD', 's3'], '3b': ['wos', 'BC', 208], '1g': ['wf', 'IR', 's4']},
{'3a': ['chemia', 'Ma', 15], '1d': ['wf', 'MM', 's1'], '2c': ['biologia', 'Wa', 213], '1a': ['informatyka', 'KI', 206], '2b': ['j.angielski', 'EP', 103], '2g': ['historia', 'PE', 106], '2e': ['matematyka', 'KT', 203], '3d': ['j.polski', 'AM', 109], '3e': ['j.niemiecki', 'GW', 107], '3c': ['matematyka', 'AR', 115], '1c': ['matematyka', 'BP', 316], '1b': ['religia', 'WK', 7], '1f': ['historia', 'HV', 108], '3b': ['geografia', 'CK', 216], '1e': ['matematyka', 'MR', 304], '1g': ['j.angielski', 'RR', 208], '2d': ['religia', 'GP', 105], '3f': ['j.rosyjski', 'ER', 205], '2a': ['fizyka', 'ŁS', 23]},
{'2c': ['matematyka', 'MR', 15], '3c': ['j.polski', 'MJ', 213], '2b': ['j.angielski', 'EP', 206], '2e': ['j.polski', 'AM', 103], '2g': ['j.angielski', 'BH', 106], '1a': ['historia', 'HW', 203], '1e': ['informatyka', 'KI', 109], '3e': ['historia', 'HV', 107], '3a': ['j.angielski', 'KJ', 115], '1d': ['j.łac', 'Sz', 316], '3d': ['wf', 'IR', 's1'], '1g': ['j.angielski', 'RR', 7], '1c': ['biologia', 'Wa', 108], '2d': ['j.polski', 'MK', 216], '1f': ['religia', 'WK', 304], '2a': ['pp', 'BC', 208], '3b': ['matematyka', 'KT', 105], '3f': ['wf', 'MM', 's2'], '1b': ['j.angielski', 'RP', 205]},
{'2c': ['matematyka', 'MR', 15], '1g': ['j.polski', 'AM', 213], '2d': ['j.polski', 'MK', 206], '2b': ['wf', 'MM', 's1'], '1d': ['historia', 'HW', 103], '2g': ['fizyka', 'ŁS', 106], '2e': ['matematyka', 'KT', 203], '3d': ['historia', 'VR', 109], '3e': ['j.polski', 'PS', 107], '1e': ['j.niemiecki', 'MW', 115], '3c': ['j.polski', 'MJ', 316], '1c': ['matematyka', 'BP', 7], '1a': ['j.angielski', 'RR', 108], '1f': ['historia', 'HV', 216], '3a': ['chemia', 'Ma', 304], '2a': ['geografia', 'Wg', 208], '3b': ['wf', 'KS', 's2'], '1b': ['wf', 'IR', 's3'], '3f': ['j.rosyjski', 'ER', 105]},
{'1g': ['matematyka', 'MV', 15], '1d': ['geografia', 'ŁS', 213], '2d': ['historia', 'PE', 206], '2b': ['historia', 'HW', 103], '2c': ['j.polski', 'PS', 106], '2a': ['j.polski', 'AM', 203], '2g': ['j.rosyjski', 'ER', 109], '2e': ['religia', 'WK', 107], '1c': ['j.polski', 'RS', 115], '1e': ['j.polski', 'MK', 316], '3c': ['j.angielski', 'BH', 7], '3e': ['fizyka', 'MB', 108], '3a': ['wf', 'MM', 's1'], '3d': ['j.niemiecki', 'KJ', 216], '1f': ['informatyka', 'DD', 304], '3f': ['matematyka', 'AT', 208], '1a': ['j.angielski', 'RR', 105], '1b': ['wf', 'IR', 's2'], '3b': ['j.angielski', 'EP', 205]},
{'2e': ['fizyka', 'ŁS', 15], '2c': ['informatyka', 'DD', 213], '2g': ['matematyka', 'AR', 206], '2d': ['j.angielski', 'BH', 103], '2a': ['wf', 'HR', 's1'], '2b': ['j.angielski', 'EP', 106], '1d': ['j.polski', 'PS', 203], '1g': ['j.polski', 'AM', 109], '1f': ['j.niemiecki', 'ER', 107], '1c': ['j.polski', 'RS', 115], '1e': ['j.niemiecki', 'MW', 316], '1a': ['matematyka', 'BP', 7], '1b': ['j.polski', 'MK', 108]},
{'2e': ['j.niemiecki', 'ER', 15], '2d': ['historia', 'PE', 213], '2b': ['fizyka', 'ŁS', 206], '2a': ['matematyka', 'BP', 103], '2c': ['religia', 'WK', 106]},
{}]]

 
  }},
  methods: {
    handleSubmit() {
      router.push("/step/1")
    },
    planClass() {
      this.selectedPlans="class"
    },
    planTeacher() {
      this.selectedPlans="teacher"
    },
    planClassroom() {
      this.selectedPlans="classroom"
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