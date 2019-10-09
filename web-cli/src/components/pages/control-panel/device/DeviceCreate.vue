<template>
  <div>
    <app-logo title="Devices - Create"/>

    <section class="section section-padding">
      <form method="post" @submit.prevent="submit">
        <div class="field">
          <label class="label">Name</label>
          <div class="control">
            <input
              class="input"
              type="text"
              name="name"
              placeholder="e.g. Device X"
              v-model="formData.name"
            >
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
  name: "DeviceCreate",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {
        name: ""
      }
    };
  },
  methods: {
    submit() {
      this.isLoading = true;

      let data = this.formData;

      this.$http({
        url: "/api/device/create",
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
              message: "Device was created"
            });

            this.$router.push("/control-panel/device");
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
      this.$router.push("/control-panel/device");
    }
  }
};
</script>

<style scoped>
</style>
