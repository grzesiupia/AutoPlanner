<template>
  <div>
      <label style="font-size:50px;display: block;text-align:center">Zarejestruj się</label>
    <form class=topform>
      <p><input v-model="email" type="email" placeholder="Email"></p>
      <p><input v-model="username" type="text" placeholder="Nazwa użytkownika"></p>
      <p><input v-model="password" type="password" placeholder="Hasło"></p>
      <label class="alert" v-show="success !== true">{{errorMessage}}</label>
      <input class="buttonm btn btn-success mr-3" type="submit" @click="handleSubmit" value="Zarejestruj">
    </form>
    </div>
</template>

<script>

export default {
  name: "Register",
  data: function() {
    return {
        email: "",
        password: "",
        username: "",
    };
  },
  computed: {
    success() {
      return this.$store.getters.getRegisterSuccess;
    },
    errorMessage() {
      return this.$store.getters.getRegisterError;
    }
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.$store.dispatch(
        "register",
        { email: this.email ,
        username: this.username,
        password: this.password,
        }
      );
       this.$store.commit("SET_EMAIL",this.email);
      }
  },
};
</script>


<style scoped>
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
.labela
{
display: block;
text-align:left;
margin-left:25%;
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
  margin-right: 25%;
  margin-bottom:20px
}
.topform
{
  position:relative;
  margin-bottom:10px;
  text-align: center;
  
}
textarea
{
  width: 50%;
}
input[type=text],input[type=password],input[type=email],input[type=tel], select {
  width: 50%;
  padding: 12px 20px;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
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
  input[type=text],input[type=password],input[type=email],input[type=tel], select,textarea 
  {
  width: 80%;
  }
  .labela
  {
  margin-left:10%;
  }
}

</style>