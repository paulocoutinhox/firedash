<template>
  <div>
    <app-logo title="Devices - Update" />

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
            />
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
  name: "DeviceUpdate",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {
        name: "",
        token: ""
      }
    };
  },
  methods: {
    refresh() {
      this.isLoading = true;

      let data = {
        id: this.$route.params.id
      };

      this.$http({ url: "/api/device/get", data: data, method: "POST" })
        .then(resp => {
          if (resp.data.success) {
            this.formData = resp.data.data.device;
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
      data.id = this.$route.params.id;

      this.$http({
        url: "/api/device/update",
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
              message: "Device was updated"
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
    generateToken() {
      this.formData.token = this.$uuid.v4();
    },
    back() {
      this.$router.push("/control-panel/device");
    }
  },
  mounted() {
    this.refresh();
  }
};
</script>

<style scoped>
</style>
