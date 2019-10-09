<template>
  <div>
    <app-logo title="Profile - Update"/>

    <section class="section section-padding">
      <form method="post" @submit.prevent="submit">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input" type="text" name="name" v-model="formData.name">
          </div>
        </div>

        <div class="field">
          <label class="label">E-mail</label>
          <div class="control">
            <input class="input" type="text" name="email" v-model="formData.email">
          </div>
        </div>

        <div class="field">
          <label class="label">Photo URL</label>
          <div class="control">
            <input class="input" type="text" name="email" v-model="formData.photo_url">
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
  name: "ProfileUpdate",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {
        name: "",
        email: "",
        photo_url: ""
      }
    };
  },
  methods: {
    refresh() {
      this.isLoading = true;

      this.$http({ url: "/api/auth/get", data: {}, method: "POST" })
        .then(resp => {
          if (resp.data.success) {
            this.formData = resp.data.data.account;
            this.isLoading = false;
          } else {
            this.$buefy.toast.open({
              position: "is-bottom",
              type: "is-danger",
              message: this.getResponseMessage()
            });

            this.back();
          }
        })
        .catch(err => {
          this.$buefy.toast.open({
            position: "is-bottom",
            type: "is-danger",
            message: this.getResponseMessage()
          });

          this.back();
        });
    },
    submit() {
      this.isLoading = true;

      let data = this.formData;

      this.$http({
        url: "/api/auth/update",
        data: data,
        method: "POST"
      })
        .then(resp => {
          if (resp.data.success) {
            this.$store.commit("profileUpdated", {
              account: resp.data.data.account
            });

            this.isLoading = false;

            this.$buefy.toast.open({
              position: "is-bottom",
              type: "is-success",
              message: "Profile was updated"
            });

            this.back();
          } else {
            this.isLoading = false;

            this.$buefy.toast.open({
              position: "is-bottom",
              type: "is-danger",
              message: this.getResponseMessage(resp.data)
            });
          }
        })
        .catch(err => {
          this.isLoading = false;

          this.$buefy.toast.open({
            position: "is-bottom",
            type: "is-danger",
            message: this.getResponseMessage()
          });
        });
    },
    back() {
      this.$router.push("/control-panel");
    }
  },
  mounted() {
    this.refresh();
  }
};
</script>

<style scoped>
</style>
