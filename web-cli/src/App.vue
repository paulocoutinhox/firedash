<template>
  <div id="app" class="container is-fluid">
    <app-header></app-header>
    <router-view/>
  </div>
</template>

<script>
import AppHeader from "@/components/app/AppHeader";

export default {
  name: "App",
  components: {
    AppHeader
  },
  created: function() {
    this.$http.interceptors.response.use(undefined, function(err) {
      return new Promise(function(resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(logout);
        }
        throw err;
      });
    });
  }
};
</script>

<style scoped>
#app {
  margin-top: 13px;
}
</style>

<style lang="scss">
@import "scss/custom-bulma";
</style>