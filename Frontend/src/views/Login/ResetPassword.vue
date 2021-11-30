<template>
  <div >
    <h1 style="display: block;text-align:center">Wpisz swój email, aby odzyskać hasło</h1>
    <form class=topform>
      <p><input v-model="email" type="email" placeholder="Email"></p>
      <label class="alert" v-show="success !== true">{{errorMessage}}</label>
      <input class="buttonm btn btn-success mr-3" type="submit" @click="sendPin" value="Odzyskaj hasło">
    </form>
  </div>
</template>

<script>
export default {
  name: 'ResetPassword',
  computed: {
    success() {
      return this.$store.getters.getSendPinSuccess;
    },
    errorMessage() {
      return this.$store.getters.getSendPinError;
    },
    },
    data: function() {
    return {
      email: ""
    }
  },

  methods: {
      sendPin(e)
      {
        e.preventDefault();
          this.$store.dispatch("recoverPassword",{ email: this.email});
      }
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