<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 2 - Dodaj nauczycieli</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons style="overflow-y: scroll;height: 80%;overflow-x: hidden">
    <br>
        <my-component v-for="teacher in teachers" :key="teacher.surname">
          <input class="buttonm btn btn-success mr-3" type="button" v-model="teacher.name" @click="editTeacher(teacher)">
        </my-component>
    </p></b>
    <a>
    <form class=topform @submit="addTeacher">
      <p><input id="Name" v-model="name" type="text" placeholder="Imię i Nazwisko" required></p>
      <p><input id="Email" v-model="email" type="email" placeholder="Email" required></p>
      <label style="float:left;">Prowadzone przedmioty</label>
      
      <div v-for="index in subjectNumber" :key="index">
      <p>
      <select name="subjects" id="subjects" v-model="list_of_subjects[index-1].name">
        <option disabled selected value> -- wybierz przedmiot -- </option>
        <option v-for="subject in subjects" v-bind:key="subject.subject_name" >
        {{ subject.subject_name }}
        </option>
    </select>
    
    </p>
    </div>
      <input class="buttond" type="button" @click="addSubject" value="+" >
      <input class="buttond" type="button" value="-" @click="delSubject" style="margin: 0px 8px">
      <input class="buttonf btn btn-success mr-3" type="submit" value="Dodaj">
    </form>
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="handleSubmit" value="Przejdź dalej">
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="back" value="Poprzedni krok">
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="sendPolls" value="Wyślij ankiety">
    <label class="alert" v-show="sendEmailSuccess== true">Wysłano e-maile z ankietami do nauczycieli</label>
    </a>
    </h1>
  </div>
</template>

<script>
import router from '../../router/index.js'
export default {
  name: 'Step2',
  computed: {
    sendEmailSuccess(){
      return this.$store.getters.getSendEmailsSuccess;
    },
    addSuccess(){
      return this.$store.getters.getAddTeacherSuccess;
    },
    addError(){
      return this.$store.getters.getAddTeacherError;
    },
    getSuccess(){
      return this.$store.getters.getTeachersSuccess;
    },
    getError(){
      return this.$store.getters.getTeachersError;
    },
    teachers(){
      return this.$store.getters.getTeachers;
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
    this.$store.dispatch("fetchTeachers",{ token:this.token});
    this.$store.dispatch("fetchSubjects",{ token:this.token});
    this.$store.commit("SEND_EMAILS_SUCCESS", false)
  },
   data: function() {
    return {
        subjectNumber: 1,
        name: "",
        email: "",
        list_of_subjects: [{"name":''}]
    };
  },
  methods: {
    handleSubmit() {
      router.push("/step/3")
    },
    back() {
      router.push("/step/1")
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
    addTeacher(e)
    {
       e.preventDefault();
       this.$store.dispatch(
        "sendTeacher",
        {
          token: this.token,
          name: this.name,
          email: this.email,
          list_of_subjects:this.list_of_subjects
        }
      )
    },
    editTeacher(teacher){
      this.$store.commit("SET_TEACHER",teacher)
      router.push("/edit/teacher")
    },
     sendPolls(e){
      e.preventDefault();
       this.$store.dispatch(
        "sendPolls",
        {
          token: this.token,
        }
      )
    }
  }
}
</script>

<style scoped>
.alert {
  padding: 15px 00px 15px 0px;
  font-size: 20px;
  background-color: #007e0085;
  color: white;
  display: block;
  width: 100%;
  margin-bottom: 20px;
  text-align: center;
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
.buttond
{
  float:left;
  margin-bottom: 10px;
  font-size: 20px;
}
.buttonf
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
