<template>
  <div id="app">
    <app-header></app-header>
    <app-page></app-page>
    <app-footer></app-footer>
  </div>
</template>
<script>
import Footer from "./Footer";
import Header from "./Header";
import Page from "./Page";

export default {
  components: {
    appFooter: Footer,
    appHeader: Header,
    appPage: Page
  }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
