<template>
  <div>
    <VueApexCharts :height="height" type="line" :options="chartOptions" :series="chartData" />
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
      defaultOptions: {
        title: "My chart",
        interval: 10000,
        legend: {
          enabled: true
        },
        labels: {
          enabled: true,
          type: "datetime",
          format: "H:mm:ss"
        }
      },
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
          show: true,
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
          if (response && response.data.success) {
            let datasets = response.data.data.datasets;
            let labels = response.data.data.labels;
            let chartData = [];

            for (var x = 0; x < labels.length; x++) {
              if (this.mergedOptions.labels.enabled) {
                if (this.mergedOptions.labels.type == "datetime") {
                  labels[x] = this.$moment(labels[x]).format(
                    this.mergedOptions.labels.format
                  );
                } else {
                  labels[x] = labels[x];
                }
              } else {
                labels[x] = "";
              }
            }

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
          }
        })
        .catch(error => {
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  },
  computed: {
    mergedOptions() {
      return {
        ...this.defaultOptions,
        ...this.options
      };
    }
  },
  mounted() {
    this.timers.getRemoteData.time = this.mergedOptions.interval;
    this.$timer.start("getRemoteData");

    this.chartOptions.legend.show = this.mergedOptions.legend.enabled;
  }
};
</script>

<style scoped>
</style>