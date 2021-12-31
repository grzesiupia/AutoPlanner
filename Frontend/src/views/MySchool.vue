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
    <tr v-for="n in 5" :key="n">
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
    classPlan(){
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
      plan2:[]
    };
  },
  mounted() {
        this.plan2 = this.classPlan
  },
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