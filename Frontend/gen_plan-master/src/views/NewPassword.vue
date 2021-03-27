<template>
  <div >
    <h1 style="display: block;text-align:center">Pin do zmiany hasła został wysłany na twój adres email</h1>
    <h1 style="display: block;text-align:center">Wprowadź go i ustaw nowe hasło</h1>
    <form class=topform>
      <p><input v-model="pin" type="text" placeholder="Pin"></p>
      <p><input v-model="newPass" type="password" placeholder="Hasło"></p>
      <p><input v-model="passConf" type="password" placeholder="Potwierdź hasło"></p>
      <label class="alert" v-show="success !== true">{{errorMessage}}</label>
      <input class="buttonm btn btn-success mr-3" type="submit" @click='ResetPassword' value="Potwierdź nowe hasło" :disabled="isDisabled">
    </form>
  </div>
</template>

<script>
export default {
  name: 'NewPassword',
  computed: {
    success() {
      return this.$store.getters.getNewPassSuccess;
    },
    errorMessage() {
      return this.$store.getters.getNewPassError;
    },
    isDisabled() {
        return !(this.newPass===this.passConf)||(this.newPass==="");
      },
    },
    data: function() {
    return {
      pin: "",
      newPass: "",
      passConf: "",
    }
  },
   methods: {
     ResetPassword(e) {
      e.preventDefault();
      
      this.$store.dispatch("resetPassword",{
         token: this.pin,
         password: this.newPass
         });
     },
  }
}
</script>

<style scoped>
.labela
{
display: block;
text-align:left;
margin-left:25%;
}
.alert {
  padding: 15px 00px 15px 0px;
  font-size: 20px;
  background-color: #f4433685;
  color: white;
  display: block;
  width: 50%;
  margin-left: 25%;
  margin-right: 25%;
  margin-bottom: 20px;
  text-align: center;
}
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
.topform
{
  position:relative;
  margin-bottom:10px;
}
input[type=text],input[type=password],input[type=email], select {
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  width: 50%;
  margin-left: 25%;
  margin-right: 25%
}


div {
  border-radius: 5px;
  background-color: #fdfdfd;
  padding: 20px;
}
@media screen and (max-width: 1200px) 
{
  .buttonm
  {
    width: 80%;
    margin-left: 10%;
    margin-right: 10%;
  }
  input[type=text],input[type=password],input[type=email],input[type=tel], select 
  {
  width: 80%;
  margin-left: 10%;
  margin-right: 10%;
  }
}

</style>