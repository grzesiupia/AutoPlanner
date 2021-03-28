<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 4 - Dodaj klasy</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons>
    <br><input class="buttonm btn btn-success mr-3" value="1A">
    <input class="buttonm btn btn-success mr-3" value="1B">
    <input class="buttonm btn btn-success mr-3" value="1C">
    </p></b>
    <a>
    <form class=topform>
      <p><input id="Classname" v-model="classname" type="text" placeholder="Nazwa klasy"></p>
      <p><label>Lista przedmiotów</label></p>
      <div v-for="index in subjectNumber" :key="index">
        <p style="border-left:2px solid green;border-right:2px solid green;border-bottom:2px solid green;border-top:2px solid green;">
          <select name="subjects" id="subjects" style="float:left;">
            <option disabled selected value> -- wybierz przedmiot -- </option>
            <option value="Matematyka">Matematyka</option>
            <option value="Język polski">Język polski</option>
            <option value="Historia">Historia</option>
          </select>
          <label style="font-size:16px;">Liczba godzin tygodniowo</label>
          <input type="text" class="inputsmall" style="width:20%;margin-left:10px;" placeholder="liczba godzin">
          <span style="float:right;">
          <input type="checkbox" v-model="preferedSubject" v-on:change="changePrefered">
          <select name="subjects" id="subjects" style="width:80%;">
            <option disabled selected value> -- wybierz prowadzącego -- </option>
            <option value="Matematyka">Adam Adamski</option>
            <option value="Język polski">Bartosz Bercik</option>
            <option value="Historia">Cezary Cebula</option>
          </select>
          </span>
        </p>
      </div>
      <p><input class="buttond" type="submit" @click="addSubject" value="+" ></p>
      <input class="buttonm btn btn-success mr-3" type="submit" value="Dodaj" >
    </form>
    <input class="buttonc btn btn-success mr-3"  type="submit" @click="handleSubmit" value="Przejdź dalej">
    </a>
    </h1>
  </div>
</template>


<script>
import router from '../router/index.js'
export default {
  name: 'Step4',
   data: function() {
    return {
        subjectNumber: 1,
    };
  },
  methods: {
    handleSubmit() {
      router.push("/")
    },
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
  position: absolute;
  bottom:20px;
  margin-right:50%;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  width:75%;
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