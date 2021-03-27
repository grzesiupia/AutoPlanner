<template>
  <div>
    <label style="font-size:50px;display: block;text-align:center">Nie dodałeś jeszcze żadnych danych szkoły</label>
    <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Rozpocznij dodawanie danych">
  </div>
</template>

<script>
import router from '../router/index.js'
export default {
  name: 'MySchool',
  methods: {
    handleSubmit() {
      router.push("/step/1")
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
  margin-right: 25%
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

</style>