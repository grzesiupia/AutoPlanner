<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Edycja danych sali</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons style="overflow-y: scroll;height: 80%;overflow-x: hidden">
    <br>
        <my-component v-for="classroom in classrooms" :key="classroom.name">
          <input class="buttonm btn btn-success mr-3" type="button" v-model="classroom.classroom"  @click="editCla(classroom)">
        </my-component>
    </p></b>
    <a>
    <form class=topform onsubmit="addClassroom">
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
      <input class="buttond" type="submit" @click="addSubject" value="+" >
      <input class="buttond" type="submit" value="-" @click="delSubject" style="margin: 0px 8px">
      </div>
      <input class="buttonm btn btn-success mr-3" @click="editClassroom" type="submit" value="Zapisz zmiany" >
    </form>
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="cancel" value="Wróć bez zapisywania">
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="deleteClassroom" value="Usuń salę">
    </a>
    </h1>
  </div>
</template>

<script>
import router from '../../router/index.js'
export default {
  name: 'EditClassroom',
  computed: {
    editSuccess(){
      return this.$store.getters.getEditClassroomSuccess;
    },
    editError(){
      return this.$store.getters.getEditClassroomError;
    },
    deleteSuccess(){
      return this.$store.getters.getDeleteClassroomSuccess;
    },
    deleteError(){
      return this.$store.getters.getDeleteClassroomError;
    },
    getSuccess(){
      return this.$store.getters.getClassroomSuccess;
    },
    getError(){
      return this.$store.getters.getClassroomsError;
    },
    classroom(){
        return this.$store.getters.getClassroom;
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
  mounted() {
        this.preferedSubject= Boolean(this.classroom.list_of_subjects.length),
        this.subjectNumber= this.classroom.list_of_subjects.length,
        this.classroom_name= this.classroom.classroom,
        this.list_of_subjects= this.classroom.list_of_subjects
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
    
    cancel() {
      router.push("/step/3")
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
    editClassroom(e)
    {
      e.preventDefault();
       this.$store.dispatch(
        "editClassroom",
        {
          token: this.token,
          name: this.classroom.classroom,
          new_name: this.classroom_name,
          new_list_of_subjects: this.list_of_subjects
        }
      )
    },
    deleteClassroom(e)
    {
      e.preventDefault();
       this.$store.dispatch(
        "deleteClassroom",
        {
          token: this.token,
          name: this.classroom.classroom
        }
      )
    },
    editCla(classroom){
      this.$store.commit("SET_CLASSROOM",classroom)
      router.push("/edit/classroom")
      this.preferedSubject= Boolean(this.classroom.list_of_subjects.length),
        this.subjectNumber= this.classroom.list_of_subjects.length,
        this.classroom_name= this.classroom.classroom,
        this.list_of_subjects= this.classroom.list_of_subjects
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
-ms-overflow-style: none; 
scrollbar-width: none;
}
.mbuttons::-webkit-scrollbar {
  display: none;
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