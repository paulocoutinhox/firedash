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
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
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

      let requestData = this.options.request.data
        ? this.options.request.data
        : {};

      this.$http
        .post(this.options.request.url, requestData)
        .then(response => {
          let datasets = response.data.data.datasets;
          let labels = response.data.data.labels;
          let chartData = { labels: labels, datasets: [] };

          for (var x = 0; x < datasets.length; x++) {
            let title = this.options.title[x];
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

    this.renderChart(this.chartData, this.chartOptions);
  }
};
</script>

<style scoped>
</style>