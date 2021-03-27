<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light pl-5 pr-5 fixed-top">
  <router-link to="/">
      <img src="../assets/logo.png" style="width:50px;height:50px;" />
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
      <div v-if="isLogged">
      <router-link to="/login">
        <button type="button" class="btn btn-success mr-3" >Logowanie</button>
      </router-link>
      <router-link to="/register">
        <button type="button" class="btn btn-success mr-3" >Rejestracja</button>
      </router-link>
    </div>
    <div v-else>
      <router-link to="/my/school">
        <button type="button" class="btn btn-success mr-3" >Moja szkoła</button>
      </router-link>
      <router-link to="/">
        <button type="button" class="btn btn-success mr-3" v-on:click='handleSubmit'>Wyloguj</button>
      </router-link>
    </div>
    </div>
  </nav>
</template>


<script>

export default {
  computed: {
    isLogged() {
      return this.$store.getters.getIsLogged;
    }
  },
   methods: {
    handleSubmit() {
      this.$store.commit("LOGOUT",true)
    },
  }
};
</script>


<style>
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

.navlink {
  padding: 5px;
  margin: 3px;
}


</style>