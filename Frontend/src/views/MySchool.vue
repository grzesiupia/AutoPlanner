<template>
  <div>
    <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Rozpocznij dodawanie danych">
    <div v-if="success">
      <p><input class="buttonk btn btn-success mr-3" type="submit" @click="planClass" value="Plany dla klas">
      <input class="buttonk btn btn-success mr-3" type="submit" @click="planTeacher" value="Plany dla nauczycieli">
      <input class="buttonk btn btn-success mr-3" type="submit" @click="planClassroom" value="Plany dla sal">
      </p>
<div v-if="this.selectedPlans==='class'">
  <p><label style="font-size:16px;">Przedmiot</label><input type="checkbox" v-model="sub1">
  <label style="font-size:16px;">Nauczyciel</label><input type="checkbox" v-model="teach1">
  <label style="font-size:16px;">Sala</label><input type="checkbox" v-model="classr1">
  </p>
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
    <tr v-for="n in classPlan[0].length" :key="n">
       <th scope="row">{{n}}</th>  
       <td v-for="(p,i) in classPlan" :key="i">
         <div v-if="classPlan[i][n-1] && m.name in classPlan[i][n-1] && sub1">{{classPlan[i][n-1][m.name][0]}}</div><div v-else></div>
         <div v-if="classPlan[i][n-1] && m.name in classPlan[i][n-1] && teach1">{{classPlan[i][n-1][m.name][1]}}</div><div v-else></div>
         <div v-if="classPlan[i][n-1] && m.name in classPlan[i][n-1] && classr1">{{classPlan[i][n-1][m.name][2]}}</div><div v-else></div>
         </td>
    </tr>
   </tbody>
</table>
</div>
<div v-if="this.selectedPlans==='teacher'">
  <p><label style="font-size:16px;">Przedmiot</label><input type="checkbox" v-model="sub2">
  <label style="font-size:16px;">Klasa</label><input type="checkbox" v-model="cla2">
  <label style="font-size:16px;">Sala</label><input type="checkbox" v-model="classr2">
  </p>
  <table class="table table-striped" v-for="(m,ii) in this.teachers" :key="ii" >
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
    <tr v-for="n in classPlan[0].length" :key="n">
       <th scope="row">{{n}}</th>  
       <td v-for="(p,i) in teacherPlans" :key="i">
         <div v-if="teacherPlans[i][n-1] && m.name in teacherPlans[i][n-1] && sub2">{{teacherPlans[i][n-1][m.name][0]}}</div><div v-else></div>
         <div v-if="teacherPlans[i][n-1] && m.name in teacherPlans[i][n-1] && cla2">{{teacherPlans[i][n-1][m.name][1]}}</div><div v-else></div>
         <div v-if="teacherPlans[i][n-1] && m.name in teacherPlans[i][n-1] && classr2">{{teacherPlans[i][n-1][m.name][2]}}</div><div v-else></div>
         </td>
    </tr>
   </tbody>
</table>
</div>
<div v-if="this.selectedPlans==='classroom'">
  <p><label style="font-size:16px;">Przedmiot</label><input type="checkbox" v-model="sub3">
  <label style="font-size:16px;">Nauczyciel</label><input type="checkbox" v-model="teach3">
  <label style="font-size:16px;">Klasa</label><input type="checkbox" v-model="cla3">
  </p>
  <table class="table table-striped" v-for="(m,ii) in this.classrooms" :key="ii" >
  <thead>
    <tr>
      <th>{{m.classroom}}</th>
      <th>Poniedziałek</th>
      <th>Wtorek</th>
      <th>Środa</th>
      <th>Czwartek</th>
      <th>Piątek</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="n in classPlan[0].length" :key="n">
       <th scope="row">{{n}}</th>  
       <td v-for="(p,i) in classroomPlans" :key="i">
         <div v-if="classroomPlans[i][n-1] && m.classroom in classroomPlans[i][n-1] && sub3">{{classroomPlans[i][n-1][m.classroom][0]}}</div><div v-else></div>
         <div v-if="classroomPlans[i][n-1] && m.classroom in classroomPlans[i][n-1] && teach3">{{classroomPlans[i][n-1][m.classroom][1]}}</div><div v-else></div>
         <div v-if="classroomPlans[i][n-1] && m.classroom in classroomPlans[i][n-1] && cla3">{{classroomPlans[i][n-1][m.classroom][2]}}</div><div v-else></div>
         </td>
    </tr>
   </tbody>
</table>
</div>
  </div>
  </div>
</template>

<script>
import router from '../router/index.js'
export default {
  name: 'MySchool',
  computed: {
    success() {
      return this.$store.getters.getClassPlansSuccess;
    },
    errorMessage() {
      return this.$store.getters.getClassPlansError;
    },
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
    teachers(){
      return this.$store.getters.getTeachers;
    },
    classrooms(){
      return this.$store.getters.getClassrooms;
    },
  },
  created(){
    this.$store.dispatch("fetchClassPlans",{ token:this.token});
    this.$store.dispatch("fetchTeacherPlans",{ token:this.token});
    this.$store.dispatch("fetchClassroomPlans",{ token:this.token});
    this.$store.dispatch("fetchClasses",{ token:this.token});
    this.$store.dispatch("fetchTeachers",{ token:this.token});
    this.$store.dispatch("fetchClassrooms",{ token:this.token});
  },
  data: function() {
    return { 
      selectedPlans:"class",
      sub1:true,
      teach1:false,
      classr1:false,
      sub2:false,
      cla2:true,
      classr2:false,
      sub3:false,
      teach3:false,
      cla3:true,
    };
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
input[type=checkbox]
{
  -ms-transform: scale(2); 
  -moz-transform: scale(2); 
  -webkit-transform: scale(2); 
  -o-transform: scale(2); 
  transform: scale(2);
  margin-right:10px;
  margin-left:10px;
  margin-top:5px;
  float:center;
}
</style>