<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Krok 3 - Dodaj sale lekcyjne</label>
    <hr style="border: 1px solid green;">
    <h1 class=row2><b><p class=mbuttons>
    <br><input class="buttonm btn btn-success mr-3" value="Sala 101">
    <input class="buttonm btn btn-success mr-3" value="Sala 102">
    <input class="buttonm btn btn-success mr-3" value="Sala 103">
    </p></b>
    <a>
    <form class=topform>
      <p><input id="Classroom" v-model="classroom" type="text" placeholder="Nazwa sali"></p>
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
  name: 'Step3',
  methods: {
    handleSubmit() {
      router.push("/step/4")
    },
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