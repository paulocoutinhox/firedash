<template>
  <div>
    <app-logo title="Accounts"/>

    <section class="section section-padding">
      <b-table
        :data="listData.isEmpty ? [] : listData.data"
        :hoverable="true"
        :striped="true"
        :loading="listData.isLoading"
        :mobile-cards="true"
        default-sort="id"
        :default-sort-direction="'desc'"
      >
        <template slot-scope="props">
          <b-table-column field="id" label="ID" width="40" sortable numeric>{{ props.row.id }}</b-table-column>

          <b-table-column field="name" label="Name" sortable>{{ props.row.name }}</b-table-column>

          <b-table-column field="email" label="E-mail" sortable>{{ props.row.email }}</b-table-column>

          <b-table-column field="is_admin" label="Is admin" sortable centered>
            <span class="tag is-success" v-if="props.row.is_admin == true">yes</span>
            <span class="tag is-danger" v-else>no</span>
          </b-table-column>

          <b-table-column field="created_at" label="Created at" sortable centered>
            <span class="tag is-default" v-if="props.row.created_at">
              {{ new Date(props.row.created_at).toLocaleDateString() }}
              &nbsp;
              {{ new Date(props.row.created_at).toLocaleTimeString() }}
            </span>
            <span class="tag is-default is-italic" v-else>none</span>
          </b-table-column>

          <b-table-column field="updated_at" label="Updated at" sortable centered>
            <span class="tag is-default" v-if="props.row.updated_at">
              {{ new Date(props.row.updated_at).toLocaleDateString() }}
              &nbsp;
              {{ new Date(props.row.updated_at).toLocaleTimeString() }}
            </span>
            <span class="tag is-default is-italic" v-else>none</span>
          </b-table-column>

          <b-table-column centered>
            <div class="buttons">
              <b-button
                size="is-small"
                icon-left="mdi mdi-key"
                class="is-info"
                v-on:click="getTokenRow(props.row.id)"
              ></b-button>

              <b-button
                size="is-small"
                icon-left="mdi mdi-view-comfy"
                class="is-primary"
                v-on:click="viewRow(props.row.id)"
              ></b-button>

              <b-button
                size="is-small"
                icon-left="mdi mdi-pencil"
                class="is-warning"
                v-on:click="updateRow(props.row.id)"
              ></b-button>

              <b-button
                size="is-small"
                icon-left="mdi mdi-delete"
                class="is-danger"
                v-on:click="deleteRow(props.row.id)"
              ></b-button>
            </div>
          </b-table-column>
        </template>

        <template slot="empty">
          <section class="section">
            <div class="content has-text-grey has-text-centered">
              <p>
                <b-icon icon="emoticon-sad" size="is-large"></b-icon>
              </p>
              <p>Nothing here.</p>
            </div>
          </section>
        </template>
      </b-table>

      <div class="formButtonList">
        <b-button v-on:click="refresh" icon-left="refresh" type="is-primary">Refresh</b-button>
        <b-button v-on:click="create" icon-left="plus" type="is-primary">Create</b-button>
        <b-button v-on:click="back" icon-left="arrow-left" type="is-primary">Back</b-button>
      </div>

      <!-- modal for account token -->
      <b-modal
        :active.sync="isAccountTokenModalActive"
        has-modal-card
        full-screen
        :can-cancel="true"
      >
        <div class="modal-card" style="padding: 0 10px">
          <header class="modal-card-head">
            <p class="modal-card-title">Account token</p>
          </header>
          <section class="modal-card-body">
            <b-field>
              <b-input type="textarea" :value="accountToken"></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button
              type="is-info"
              icon-left="content-copy"
              v-clipboard:copy="accountToken"
              v-clipboard:success="onAccountTokenCopySuccess"
              v-clipboard:error="onAccountTokenCopyError"
            >Copy</b-button>
            <b-button v-on:click="isAccountTokenModalActive = false" type="is-primary">Close</b-button>
          </footer>
        </div>
      </b-modal>
    </section>
  </div>
</template>

<script>
import AppLogo from "@/components/app/AppLogo.vue";
import { util } from "@/mixins/util";

export default {
  name: "AccountHome",
  components: { AppLogo },
  mixins: [util],
  data() {
    return {
      listData: {
        data: [],
        isEmpty: false,
        isLoading: true
      },
      accountToken: "",
      isAccountTokenModalActive: false
    };
  },
  methods: {
    refresh() {
      this.listData.isLoading = true;

      this.$http({ url: "/api/account/list", data: {}, method: "POST" })
        .then(resp => {
          if (resp.data.success) {
            this.listData.data = resp.data.data.list;
            this.listData.isLoading = false;
            this.listData.isEmpty = this.listData.data.length == 0;
          } else {
            this.listData.isLoading = false;
            this.listData.isEmpty = true;
          }
        })
        .catch(err => {
          this.listData.isLoading = false;
          this.listData.isEmpty = true;
        });
    },
    deleteRow(id) {
      this.$dialog.confirm({
        message: "Are you sure?",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => {
          this.listData.isLoading = true;

          this.$http({
            url: "/api/account/delete",
            data: { id: id },
            method: "POST"
          })
            .then(resp => {
              if (resp.data.success) {
                this.refresh();

                this.$toast.open({
                  position: "is-bottom",
                  type: "is-success",
                  message: "Account was removed!"
                });
              } else {
                this.refresh();

                this.$toast.open({
                  position: "is-bottom",
                  type: "is-danger",
                  message: this.getResponseMessage(resp.data)
                });
              }
            })
            .catch(err => {
              this.refresh();

              this.$toast.open({
                position: "is-bottom",
                type: "is-danger",
                message: this.getResponseMessage()
              });
            });
        }
      });
    },
    viewRow(id) {
      this.$router.push({ name: "AccountView", params: { id: id } });
    },
    updateRow(id) {
      this.$router.push({ name: "AccountUpdate", params: { id: id } });
    },
    back() {
      this.$router.push("/control-panel");
    },
    create() {
      this.$router.push("/control-panel/account/create");
    },
    getTokenRow(id) {
      this.listData.isLoading = true;

      this.$http({
        url: "/api/account/token",
        data: { id: id },
        method: "POST"
      })
        .then(resp => {
          if (resp.data.success) {
            this.accountToken = resp.data.data.token;
            this.isAccountTokenModalActive = true;
            this.listData.isLoading = false;
          } else {
            this.listData.isLoading = false;

            this.$toast.open({
              position: "is-bottom",
              type: "is-danger",
              message: this.getResponseMessage(resp.data)
            });
          }
        })
        .catch(err => {
          this.listData.isLoading = false;

          this.$toast.open({
            position: "is-bottom",
            type: "is-danger",
            message: this.getResponseMessage()
          });
        });
    },
    onAccountTokenCopySuccess: function(e) {
      this.$toast.open({
        position: "is-bottom",
        type: "is-success",
        message: "Copied!"
      });
    },
    onAccountTokenCopyError: function(e) {
      this.$toast.open({
        position: "is-bottom",
        type: "is-danger",
        message: "Failed to copy text!"
      });
    }
  },
  mounted() {
    this.refresh();
  }
};
</script>

<style scoped>
</style>
