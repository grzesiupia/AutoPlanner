<template>
  <div>
      <label style="font-size:50px;display: block;text-align:center">Witaj ponownie!</label>
    <form class=topform>
      <p><input id="Email" v-model="email" type="email" placeholder="Email"></p>
      <p><input id="Password" v-model="pass" type="password" placeholder="Hasło"></p>
      <label class="alert" v-show="success !== true">{{errorMessage}}</label>
      <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Zaloguj">
    </form>
      <router-link to="/reset/password" class=forgotpass>Zapomniałeś hasła?</router-link>
      <router-link to="/register" class=signup>
          Nie masz konta?
          <strong>Zarejestruj się!</strong>
        </router-link>
    </div>
</template>

<script>
export default {
  
  name: "Login",
  computed: {
    success() {
      return this.$store.getters.getLoginSuccess;
    },
    errorMessage() {
      return this.$store.getters.getLoginError;
    },
  },
  data: function() {
    return {
      email: "",
      pass: "",
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.$store.dispatch(
        "login",
        { email: this.email ,
        password: this.pass }
      );
    },
  }
};
</script>


<style scoped>
.forgotpass
{
  display: block;
  text-align:left;
  margin-left:25%;
  margin-right:50%
}
.signup
{
  display: block;
  text-align:right;
  margin-right:25%;
  margin-left:50%;
  margin-top:-20px
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
  .labela
  {
  margin-left:10%;
  }
  .forgotpass
  {
  
  margin-left:10%;
  margin-right:50%
  }
  .signup
  {
  margin-right:10%;
  margin-left:50%;
  }
}

</style>