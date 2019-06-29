<template>
  <nav class="navbar is-fixed-top is-transparent" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img src="@/assets/images/logo.png" alt="Firedash" style="margin-right: 10px;">
        Firedash
      </router-link>

      <span class="navbar-burger" aria-label="menu" aria-expanded="false" v-on:click="toggleMenu()">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </span>
    </div>

    <div class="navbar-end navbar-menu" v-bind:class="{ 'is-active': menuActive }">
      <router-link
        to="/dashboards"
        class="navbar-item is-tab"
        v-on:click.native="closeMenu()"
      >Dashboards</router-link>

      <router-link
        to="/login"
        class="navbar-item is-tab"
        v-on:click.native="closeMenu()"
        v-if="!isLoggedIn"
      >Login</router-link>

      <a v-on:click="logout" v-on:click.native="closeMenu()" class="navbar-item is-tab" v-if="isLoggedIn">Logout</a>
    </div>
  </nav>
</template>

<script>
export default {
  name: "app-header",
  data() {
    return {
      menuActive: false
    };
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    currentAccount: function() {
      return this.$store.getters.account;
    }
  },
  methods: {
    toggleMenu() {
      this.menuActive = !this.menuActive;
    },
    closeMenu() {
      this.menuActive = false;
    },
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/");
      });
    }
  }
};
</script>

<style scoped>
.nav-left .nav-item img {
  margin-right: 10px;
}
.navbar {
  padding: 0 20px;
  border-bottom: 1px solid #dbdbdb;
}
</style>
