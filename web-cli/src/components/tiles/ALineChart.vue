<template>
  <div>
    <VueApexCharts :height="height" type="line" :options="chartOptions" :series="chartData"/>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "ALineChart",
  components: { VueApexCharts },
  props: {
    options: {
      type: Object,
      required: true,
      default: {}
    },
    height: {
      type: Number
    }
  },
  timers: {
    getRemoteData: {
      time: 0,
      autostart: false,
      repeat: true,
      immediate: true
    }
  },
  data() {
    return {
      loading: false,
      errored: false,
      chartOptions: {
        chart: {
          toolbar: {
            show: false
          },
          parentHeightOffset: 0
        },
        stroke: {
          curve: "smooth",
          width: 2
        },
        dataLabels: {
          enabled: false
        },
        legend: {
          position: "top",
          horizontalAlign: "right",
          floating: true
        },
        xaxis: null
      },
      chartData: []
    };
  },
  methods: {
    getRemoteData() {
      if (this.loading) {
        return;
      }

      this.loading = true;

      let requestData = this.options.request.data
        ? this.options.request.data
        : {};

      this.$http
        .post(this.options.request.url, requestData)
        .then(response => {
          let datasets = response.data.data.datasets;
          let labels = response.data.data.labels;
          let chartData = [];

          this.chartOptions = {
            ...this.chartOptions,
            ...{
              xaxis: {
                type: "category",
                categories: labels
              }
            }
          };

          for (var x = 0; x < datasets.length; x++) {
            let title = this.options.title[x];
            let items = datasets[x].items;

            chartData.push({
              name: title,
              data: items
            });
          }

          this.chartData = chartData;
          this.errored = false;
        })
        .catch(error => {
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  },
  mounted() {
    this.timers.getRemoteData.time = this.options.interval
      ? this.options.interval
      : 10000;
    this.$timer.start("getRemoteData");
  }
};
</script>

<style scoped>
</style>