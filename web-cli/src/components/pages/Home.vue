<template>
  <div>
    <app-logo/>

    <section class="section section-padding">
      <div class="columns is-centered">
        <div
          class="column is-full-mobile is-two-thirds-tablet is-two-thirds-desktop"
          style="text-align: center;"
        >
          <div v-if="isLoggedIn">
            <img :src="profileURL" style="width: 80px; border: 0;">
            <h3>Hi {{ currentAccount.name }}!</h3>
            <br>
          </div>

          <hr class="hr">

          <div v-if="isLoggedIn">
            <p>
              <router-link to="/dashboards" class="button is-primary">Go to dashboards</router-link>
            </p>
            <p v-if="isCurrentAccountAdmin">
              <br>
              <router-link to="/control-panel" class="button is-primary">Go to control panel</router-link>
            </p>

            <hr class="hr">

            <div class="formButtonList">
              <a v-on:click="logout" class="button is-danger">Logout</a>
            </div>
          </div>

          <div v-if="!isLoggedIn">
            <p>
              <router-link to="/login" class="button is-success">Login</router-link>
            </p>
          </div>

          <br>
          <br>
          <br>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";

export default {
  name: "Home",
  components: { AppLogo },
  data() {
    return {};
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    },
    currentAccount: function() {
      return this.$store.getters.currentAccount;
    },
    isCurrentAccountAdmin: function() {
      return this.$store.getters.isCurrentAccountAdmin;
    },
    profileURL: function() {
      const currentAccount = this.currentAccount;

      if (currentAccount.photo_url) {
        return currentAccount.photo_url;
      } else {
        return "/static/images/profile.png";
      }
    }
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/");
      });
    }
  }
};
</script>

<style scoped>
</style>
