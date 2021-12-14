<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 3 - Dodaj sale lekcyjne</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons>
    <br>
        <my-component v-for="classroom in classrooms" :key="classroom.name">
          <input class="buttonm btn btn-success mr-3" v-model="classroom.classroom" @click="editClassroom(classroom)">
        </my-component>
    </p></b>
    <a>
    <form class=topform @submit="addClassroom">
      <p><input id="Classroom" v-model="classroom_name" type="text" placeholder="Nazwa sali" required></p>
      <p style="margin-left:10px;"><input type="checkbox" v-model="preferedSubject" v-on:change="changePrefered"><label style="float:left;font-size:20px;">Preferowane przedmioty</label></p>
      <div v-if="preferedSubject">
      <div v-for="index in subjectNumber" :key="index" >
      <select name="subjects" id="subjects" v-model="list_of_subjects[index-1].name">
        <option disabled selected value> -- wybierz przedmiot -- </option>
        <option v-for="subject in subjects" v-bind:key="subject.subject_name" >
        {{ subject.subject_name }}
        </option>
    </select>
    </div>
    </div>
      <div v-if="preferedSubject">
      <input class="buttond" type="button" value="+" @click="addSubject">
      <input class="buttond" type="button" value="-" @click="delSubject" style="margin: 0px 8px">
      </div>
      <input class="buttonm btn btn-success mr-3" type="submit" value="Dodaj" >
    </form>
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="handleSubmit" value="Przejdź dalej">
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="back" value="Poprzedni krok">
    </a>
    </h1>
  </div>
</template>

<script>
import router from '../../router/index.js'
export default {
  name: 'Step3',
  computed: {
    addSuccess(){
      return this.$store.getters.getAddClassroomSuccess;
    },
    addError(){
      return this.$store.getters.getAddClassroomError;
    },
    getSuccess(){
      return this.$store.getters.getClassroomSuccess;
    },
    getError(){
      return this.$store.getters.getClassroomsError;
    },
    classrooms(){
      return this.$store.getters.getClassrooms;
    },
    subjects(){
      return this.$store.getters.getSubjects;
    },
    token() 
    {
      return this.$store.getters.getToken;
    },
  },
   created(){
    this.$store.dispatch("fetchClassrooms",{ token:this.token});
    this.$store.dispatch("fetchSubjects",{ token:this.token});
  },
  data: function() {
    return {
        preferedSubject:false,
        subjectNumber: 0,
        classroom_name: "",
        list_of_subjects: []
    };
  },
  methods: {
    changePrefered()
    {
      if(this.preferedSubject==false)
      {
        this.subjectNumber=0;
        this.list_of_subjects= []
      }
      else
      {
        this.subjectNumber=1;
        this.list_of_subjects=[{"name":''}]
      }
    },
    handleSubmit() {
      router.push("/step/4")
    },
    back() {
      router.push("/step/2")
    },
    addSubject(e)
    {
      e.preventDefault();
      this.subjectNumber=this.subjectNumber+1;
      this.list_of_subjects.push({"name":''})
    },
    delSubject(e)
    {
      e.preventDefault();
      if(this.subjectNumber>1)
      {
      this.subjectNumber=this.subjectNumber-1;
      this.list_of_subjects.pop()
      }
     
    },
    addClassroom(e)
    {
      e.preventDefault();
       this.$store.dispatch(
        "sendClassroom",
        {
          token: this.token,
          name: this.classroom_name,
          list_of_subjects: this.list_of_subjects
        }
      )
    },
    editClassroom(classroom){
      this.$store.commit("SET_CLASSROOM",classroom)
      router.push("/edit/classroom")
    }
  }
}
</script>

<style scoped>
input[type=checkbox]
{
  -ms-transform: scale(2); 
  -moz-transform: scale(2); 
  -webkit-transform: scale(2); 
  -o-transform: scale(2); 
  transform: scale(2);
  margin-right:10px;
  margin-top:5px;
  float:left;
}
input[type=text],input[type=password],input[type=email], select 
{
  padding: 15px 15px;
  font-size: 16px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  width: 100%;
}
.mbuttons
{
position: absolute;
left:20px;
top: 125px;
width:18%;
}
.buttonm 
{
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  width:100%;
}
.buttond
{
  float:left;
  margin-bottom: 10px;
  font-size: 20px;
}
.buttonc 
{
  margin-right:50%;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  width:100%;
}
.row2 
{
  overflow: hidden;
  width: 100%;
}
.row2 b 
{
  width: 20%;
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
.row2 a
{
  width: 75%;
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  border-left:2px solid green;
}
@media screen and (max-width: 800px) 
{
  .row2 b
  {
    float: none;
    width: 95%;
  }
  .row2 a
  {
    float: none;
    width: 95%;
    border-left:none;
  }
  .mbuttons
  {
    float: none;
    width: 100%;
    position:relative;
    top: 0px;
    left:0px;
    
  }
  .buttonc 
  {
      width:100%;
      position: relative;
      margin-top:30px;
  }
}
</style>