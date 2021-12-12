<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 4 - Dodaj klasy</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons>
    <br>
        <my-component v-for="clas in classes" :key="clas.name">
          <input class="buttonm btn btn-success mr-3" v-model="clas.class" @click="editClass(clas)">
        </my-component>
    </p></b>
    <a>
    <form class=topform onsubmit="addClass">
      <p><input id="Classname" v-model="classname" type="text" placeholder="Nazwa klasy" required></p>
      <p><label>Lista przedmiotów</label></p>
      <div v-for="index in lessonsNumber" :key="index" >
        <p style="border-left:2px solid green;border-right:2px solid green;border-bottom:2px solid green;border-top:2px solid green;">
          <select name="subjects" id="subjects" style="float:left;" v-model="list_of_lessons[index-1].name">
            <option disabled selected value> -- wybierz przedmiot -- </option>
            <option v-for="subject in subjects" v-bind:key="subject.subject_name" >
            {{ subject.subject_name }}
            </option>
          </select>
          <label style="font-size:16px;">Liczba godzin tygodniowo</label>
          <input type="text" class="inputsmall" style="width:20%;margin-left:10px;" placeholder="liczba godzin" v-model="list_of_lessons[index-1].number">
          <span style="float:right;">
          <input type="checkbox" v-on:change="changePref(index)">
          <select name="teachers" id="teachers" style="width:80%;" v-model="list_of_lessons[index-1].teacher" :disabled="disabled[index-1] == 1">
            <option disabled selected value> -- wybierz prowadzącego -- </option>
            <option v-for="teacher in teachers" v-bind:key="teacher.name" >
            {{ teacher.name }}
            </option>
          </select>
          </span>
        </p>
      </div>
      <p><input class="buttond" type="submit" @click="addSubject" value="+" >
      <input class="buttond" type="submit" value="-" @click="delSubject" style="margin: 0px 8px"></p>
      <input class="buttonm btn btn-success mr-3"  type="submit" value="Dodaj" >
    </form>
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="handleSubmit" value="Przejdź dalej">
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="back" value="Poprzedni krok">
    </a>
    </h1>
  </div>
</template>


<script>
import Vue from 'vue';
import router from '../../router/index.js'
export default {
  name: 'Step4',
  computed: {
    addSuccess(){
      return this.$store.getters.getAddClassSuccess;
    },
    addError(){
      return this.$store.getters.getAddClassError;
    },
    getSuccess(){
      return this.$store.getters.getClassSuccess;
    },
    getError(){
      return this.$store.getters.getClassesError;
    },
    classes(){
      return this.$store.getters.getClasses;
    },
    subjects(){
      return this.$store.getters.getSubjects;
    },
    teachers(){
      return this.$store.getters.getTeachers;
    },
    token() 
    {
      return this.$store.getters.getToken;
    },
  },
  created(){
    this.$store.dispatch("fetchClasses",{ token:this.token});
    this.$store.dispatch("fetchSubjects",{ token:this.token});
    this.$store.dispatch("fetchTeachers",{ token:this.token});
  },
   data: function() {
    return {
        lessonsNumber: 1,
        classname: "",
        list_of_lessons: [{"name":'',"number":'',"teacher":''}],
        disabled: [1],
    };
  },
  methods: {
    handleSubmit() {
      router.push("/")
    },
    back() {
      router.push("/step/3")
    },
    addSubject(e)
    {
       e.preventDefault();
      this.lessonsNumber=this.lessonsNumber+1;
      this.list_of_lessons.push({"name":'',"number":'',"teacher":''})
      this.disabled.push(1)
    },
    delSubject(e)
    {
      e.preventDefault();
      if(this.lessonsNumber>1)
      {
      this.lessonsNumber=this.lessonsNumber-1;
      this.list_of_lessons.pop()
      this.disabled.pop()
      }
    },
    addClass(e)
    {
      e.preventDefault();
       this.$store.dispatch(
        "sendClass",
        {
          token: this.token,
          name: this.classname,
          list_of_lessons: this.list_of_lessons
        }
      )
    },
    editClass(clas){
      this.$store.commit("SET_CLASS",clas)
      router.push("/edit/class")
    },
    changePref(index)
    {
      Vue.set(this.disabled,[index-1],(this.disabled[index-1] + 1) % 2)
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
  margin-left:10px;
  margin-top:5px;
  
}
.buttond
{
  
  margin-bottom: 10px;
  font-size: 30px;
}
select
{
  padding: 10px 10px;
  font-size: 16px;
  margin: 8px 8px;
  margin-bottom: 10px;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  width: 20%;
}
input[type=text],input[type=password],input[type=email]
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