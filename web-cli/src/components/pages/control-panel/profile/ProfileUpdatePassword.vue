<template>
  <div>
    <app-logo title="Profile - Update password"/>

    <section class="section section-padding">
      <form method="post" @submit.prevent="submit">
        <div class="field">
          <label class="label">Old password</label>
          <div class="control">
            <input
              class="input"
              type="password"
              name="old_password"
              v-model="formData.old_password"
            >
          </div>
        </div>

        <div class="field">
          <label class="label">New password</label>
          <div class="control">
            <input class="input" type="password" name="password" v-model="formData.password">
          </div>
        </div>

        <div class="field">
          <label class="label">Repeat password</label>
          <div class="control">
            <input
              class="input"
              type="password"
              name="repeat_password"
              v-model="formData.repeat_password"
            >
          </div>
        </div>

        <div class="formButtonList">
          <div class="field">
            <p class="control">
              <b-button native-type="submit" icon-left="mdi mdi-pencil" type="is-primary">Update</b-button>
              <b-button icon-left="arrow-left" type="is-primary" v-on:click="back">Back</b-button>
            </p>
          </div>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";
import { util } from "@/mixins/util";

export default {
  name: "ProfileUpdatePassword",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {
        old_password: "",
        password: "",
        repeat_password: ""
      }
    };
  },
  methods: {
    submit() {
      this.isLoading = true;

      let data = this.formData;

      this.$http({
        url: "/api/auth/update-password",
        data: data,
        method: "POST"
      })
        .then(resp => {
          if (resp.data.success) {
            this.isLoading = false;

            this.$toast.open({
              position: "is-bottom",
              type: "is-success",
              message: "Your password was updated"
            });

            this.back();
          } else {
            this.isLoading = false;

            this.$toast.open({
              position: "is-bottom",
              type: "is-danger",
              message: this.getResponseMessage(resp.data)
            });
          }
        })
        .catch(err => {
          this.isLoading = false;

          this.$toast.open({
            position: "is-bottom",
            type: "is-danger",
            message: this.getResponseMessage()
          });
        });
    },
    back() {
      this.$router.push("/control-panel");
    }
  }
};
</script>

<style scoped>
</style>
