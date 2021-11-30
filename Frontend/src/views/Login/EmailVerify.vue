<template>
  <div >
    <h1 style="display: block;text-align:center">Token został wysłany na twój adres email</h1>
    <h1 style="display: block;text-align:center">Wprowadź go, aby ukończyć zajestrację</h1>
    <form class=topform>
      <p><input v-model="emailTemp" type="email" placeholder="Email"></p>
      <p><input v-model="token" type="text" placeholder="Token"></p>
      <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Potwierdź token">
    </form>
    <router-link :to='this.$route' v-on:click.native="ResendToken" class=resend>
    Nie dostałeś maila?
    <strong>Wyślij ponownie</strong></router-link>
    <label class="alert" v-show="success !== true">{{errorMessage}}</label>
    <label class="alert" v-show="resendSuccess !== true">{{resendErrorMessage}}</label>
  </div>
</template>

<script>
export default {
  name: 'EmailVerify',
  computed: {
    email(){
        return this.$store.getters.getEmail;
    },
    success() {
      return this.$store.getters.getRegisterVerifySuccess;
    },
    errorMessage() {
      return this.$store.getters.getRegisterVerifyError;
    },
    resendSuccess() {
      return this.$store.getters.getResendTokenSuccess;
    },
    resendErrorMessage() {
      return this.$store.getters.getResendTokenError;
    }
  },
    data: function() {
    return {
      token: "",
      emailTemp: ""
    }
  },
  mounted() {
    this.emailTemp = this.email
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.$store.dispatch(
        "verifyEmail",
        { email: this.emailTemp ,
        token: this.token }
      );
    },
  ResendToken() {
      this.$store.dispatch(
        "resendToken",
        { email: this.emailTemp}
      );
    }
  }
}
</script>

<style scoped>
.resend
{
  display: block;
  text-align:left;
  margin-left:25%;
  margin-right:50%
}
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
  .resend
  {
    margin-left:10%;
  }
}

</style>