<template>
  <table style="margin: 0 auto; border: 0;">
    <tr>
      <td style="vertical-align: middle;">
        <img
          src="@/assets/images/logo.png"
          title="Firedash logo"
          style="width: 50px; height: 50px;"
        >
      </td>
      <td>&nbsp;</td>
      <td style="vertical-align: middle;">
        <h1 class="title">{{ title }}</h1>
      </td>
    </tr>
  </table>
</template>

<script>
export default {
  name: "app-logo",
  props: {
    title: {
      type: String,
      default: "Firedash"
    }
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
