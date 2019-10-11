<script>
import { Line, mixins } from "vue-chartjs";
import { color } from "@/mixins/color";
import { util } from "@/mixins/util";

export default {
  extends: Line,
  mixins: [color, mixins.reactiveData, util],
  props: {
    options: {
      type: Object,
      required: true,
      default: {}
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
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: true
        }
      }
    };
  },
  created() {
    this.shuffleArray(this.chartColors);
  },
  methods: {
    getRemoteData() {
      if (this.loading) {
        return;
      }

      this.loading = true;

      let requestData = this.mergedOptions.request.data
        ? this.mergedOptions.request.data
        : {};

      this.$http
        .post(this.mergedOptions.request.url, requestData)
        .then(response => {
          if (response && response.data.success) {
            let datasets = response.data.data.datasets;
            let labels = response.data.data.labels;

            for (var x = 0; x < labels.length; x++) {
              if (this.mergedOptions.labels.enabled) {
                if (this.mergedOptions.labels.type == "datetime") {
                  labels[x] = this.$moment(labels[x]).local().format(
                    this.mergedOptions.labels.format
                  );
                } else {
                  labels[x] = labels[x];
                }
              } else {
                labels[x] = "";
              }
            }

            let chartData = { labels: labels, datasets: [] };

            for (var x = 0; x < datasets.length; x++) {
              let title = this.mergedOptions.title[x];
              let items = datasets[x].items;

              chartData.datasets.push({
                label: title,
                backgroundColor: this.chartColors[x],
                borderColor: this.chartColors[x],
                fill: false,
                borderWidth: 1,
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

    this.chartOptions.legend.display = this.mergedOptions.legend.enabled;

    this.renderChart(this.chartData, this.chartOptions);
  }
};
</script>

<style scoped>
</style>