<template>
  <div>
    <app-logo title="Firedash - Login"/>

    <section class="section section-padding">
      <div class="columns is-centered">
        <div class="column is-full-mobile is-two-thirds-tablet is-two-thirds-desktop">
          <form method="post" @submit.prevent="submit">
            <div class="field">
              <label class="label">Email</label>
              <div class="control has-icons-left has-icons-right">
                <input
                  class="input"
                  type="email"
                  name="email"
                  placeholder="e.g. my-email@gmail.com"
                  v-model="formData.email"
                >
                <span class="icon is-small is-left">
                  <i class="mdi mdi-email"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label">Password</label>
              <div class="control has-icons-left has-icons-right">
                <input
                  class="input"
                  type="password"
                  name="password"
                  placeholder="Password"
                  v-model="formData.password"
                >
                <span class="icon is-small is-left">
                  <i class="mdi mdi-lock"></i>
                </span>
              </div>
            </div>

            <div class="formButtonList">
              <div class="field">
                <p class="control" style="text-align:center;">
                  <b-button native-type="submit" type="is-success">Login</b-button>
                </p>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>

    <br>
    <br>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";
import { util } from "@/mixins/util";

export default {
  name: "Login",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      loading: false,
      isAuthenticated: false,
      formData: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    submit() {
      if (this.loading) {
        return;
      }

      this.loading = true;

      let data = {
        email: this.formData.email,
        password: this.formData.password
      };

      this.$store
        .dispatch("login", data)
        .then(() => {
          this.$router.push("/");
        })
        .catch(err => {
          this.$toast.open({
            position: "is-bottom",
            type: "is-danger",
            message: this.getResponseMessage(err, "login")
          });

          this.loading = false;
        });
    }
  }
};
</script>

<style scoped>
</style>
