<template>
  <div>
    <app-logo title="Control panel"/>

    <section class="section section-padding">
      <div class="columns is-centered">
        <div
          class="column is-full-mobile is-two-thirds-tablet is-two-thirds-desktop"
          style="text-align: center;"
        >
          <p>
            <br>
            <router-link to="/control-panel/device" class="button is-primary">Devices</router-link>
            <br>
          </p>

          <p>
            <br>
            <router-link to="/control-panel/account" class="button is-primary">Accounts</router-link>
            <br>
          </p>

          <hr class="hr" style="margin-bottom: 0;">

          <p>
            <br>
            <router-link
              to="/control-panel/profile/update"
              class="button is-primary"
            >Update my profile</router-link>
            <br>
          </p>

          <p>
            <br>
            <router-link
              to="/control-panel/profile/update-password"
              class="button is-primary"
            >Update my password</router-link>
            <br>
          </p>

          <hr class="hr">

          <div class="formButtonList">
            <router-link to="/" class="button is-primary">Back</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";

export default {
  name: "ControlPanelHome",
  components: { AppLogo }
};
</script>

<style scoped>
</style>
