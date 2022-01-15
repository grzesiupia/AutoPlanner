<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 1 - Dodaj przedmioty</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons style="overflow-y: scroll;height: 80%;overflow-x: hidden">
    <br>
        <my-component v-for="subject in subjects" :key="subject.subject_name">
          <input class="buttonm btn btn-success mr-3" type="button" v-model="subject.subject_name" @click="editSubject(subject.subject_name)">
        </my-component>
    </p></b>
    <a>
    <form class=topform @submit="addSubject">
      <p><input id="Subject" v-model="subjectName" type="text" placeholder="Nazwa przedmiotu" required></p>
      <input class="buttonm btn btn-success mr-3" type="submit" value="Dodaj">
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
  name: 'Step1',
  computed: {
    addSuccess(){
      return this.$store.getters.getAddSubjectSuccess;
    },
    addError(){
      return this.$store.getters.getAddSubjectError;
    },
    getSuccess(){
      return this.$store.getters.getSubjectsSuccess;
    },
    getError(){
      return this.$store.getters.getSubjectsError;
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
    this.$store.dispatch("fetchSubjects",{ token:this.token});
  },
  data: function(){
    return{
      subjectName:"",
    }; 
  },
  methods: {
    handleSubmit() {
      router.push("/step/2")
    },
     back() {
      router.push("/my/school")
    },
    addSubject(e){
      e.preventDefault();
      this.$store.dispatch(
        "sendSubject",
        {
          token: this.token,
          subject_name: this.subjectName
        }
      )
    },
    editSubject(subject_name){
      router.push("/edit/subject/"+subject_name)
    }
    
  }
}
</script>

<style scoped>
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
  margin-top: 4px;
  margin-right: 10px;
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
