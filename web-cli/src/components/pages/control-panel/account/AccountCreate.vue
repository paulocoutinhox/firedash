<template>
  <div>
    <app-logo title="Accounts - Create" />

    <section class="section section-padding">
      <form method="post" @submit.prevent="submit">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input class="input" type="text" name="name" v-model="formData.name" />
          </div>
        </div>

        <label class="label">Token</label>

        <div class="field is-grouped">
          <div class="control is-expanded">            
            <input
              class="input"
              type="text"
              name="token"
              placeholder="e.g. token-test"
              v-model="formData.token"
            />
          </div>
          <div class="control">
            <b-button
              native-type="button"
              icon-left="mdi mdi-plus"
              type="is-primary"
              v-on:click="generateToken"
            >Generate</b-button>
          </div>
        </div>

        <div class="field">
          <label class="label">E-mail</label>
          <div class="control">
            <input class="input" type="text" name="email" v-model="formData.email" />
          </div>
        </div>

        <div class="field">
          <label class="label">Photo URL</label>
          <div class="control">
            <input class="input" type="text" name="photo_url" v-model="formData.photo_url" />
          </div>
        </div>

        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" type="password" name="password" v-model="formData.password" />
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
            />
          </div>
        </div>

        <div class="field">
          <label class="label">Is admin</label>
          <div class="control">
            <b-checkbox v-model="formData.is_admin" true-value="1" false-value="0"></b-checkbox>
          </div>
        </div>

        <div class="formButtonList">
          <div class="field">
            <p class="control">
              <b-button native-type="submit" icon-left="mdi mdi-plus" type="is-primary">Create</b-button>
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
  name: "AccountCreate",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {
        name: "",
        token: "",
        email: "",
        photo_url: "",
        password: "",
        repeat_password: "",
        is_admin: false
      }
    };
  },
  methods: {
    submit() {
      this.isLoading = true;

      let data = this.formData;

      this.$http({
        url: "/api/account/create",
        data: data,
        method: "POST"
      })
        .then(resp => {
          if (resp.data.success) {
            this.data = resp.data.data.list;
            this.isLoading = false;

            this.$buefy.toast.open({
              position: "is-bottom",
              type: "is-success",
              message: "Account was created"
            });

            this.$router.push("/control-panel/account");
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
    generateToken() {
      this.formData.token = this.$uuid.v4();
    },
    back() {
      this.$router.push("/control-panel/account");
    }
  }
};
</script>

<style scoped>
</style>
