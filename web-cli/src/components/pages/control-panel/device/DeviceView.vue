<template>
  <div>
    <app-logo title="Devices - View"/>

    <section class="section section-padding">
      <p class="has-text-weight-bold">Name:</p>
      <p>{{ formData.name }}</p>
      <div class="formViewSeparator"></div>

      <p class="has-text-weight-bold">Created at:</p>
      <p>
        <span class="tag is-default" v-if="formData.created_at">
          {{ new Date(formData.created_at).toLocaleDateString() }}
          &nbsp;
          {{ new Date(formData.created_at).toLocaleTimeString() }}
        </span>
        <span class="tag is-default is-italic" v-else>none</span>
      </p>
      <div class="formViewSeparator"></div>

      <p class="has-text-weight-bold">Updated at:</p>
      <p>
        <span class="tag is-default" v-if="formData.updated_at">
          {{ new Date(formData.updated_at).toLocaleDateString() }}
          &nbsp;
          {{ new Date(formData.updated_at).toLocaleTimeString() }}
        </span>
        <span class="tag is-default is-italic" v-else>none</span>
      </p>
      <div class="formViewSeparator"></div>

      <div class="formButtonList">
        <div class="field">
          <p class="control">
            <b-button icon-left="arrow-left" type="is-primary" v-on:click="back">Back</b-button>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";
import { util } from "@/mixins/util";

export default {
  name: "DeviceView",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      isLoading: true,
      formData: {}
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
