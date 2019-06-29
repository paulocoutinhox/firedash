<template>
  <div>
    <div class="columns">
      <div class="column is-4-desktop is-4-tablet is-12-mobile">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">Temperature</p>
          </header>
          <div class="card-content">
            <div class="content">
              <LineChart :height="220" :options="temperatureOptions"/>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-4-desktop is-4-tablet is-12-mobile">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">Humidity</p>
          </header>
          <div class="card-content">
            <div class="content">
              <LineChart :height="220" :options="humidityOptions"/>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-4-desktop is-4-tablet is-12-mobile">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">Soil</p>
          </header>
          <div class="card-content">
            <div class="content">
              <LineChart :height="220" :options="soilOptions"/>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="columns is-desktop">
      <div class="column is-12">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">
              Realtime
              <div class="is-pulled-right" style="padding: 6px 10px 0 0;">
              <b-select
                placeholder="Moment"
                rounded
                icon="calendar"
                v-model="realtimeOptions.moment.value"
                @input="onRealtimeMomentChanged"
              >
                <option value="-5 minute">5 minutes</option>
                <option value="-30 minute">30 minutes</option>
                <option value="-1 hour">1 hour</option>
                <option value="-1 day">1 day</option>
                <option value="-7 day">7 days</option>
                <option value="-15 day">15 days</option>
                <option value="-1 month">1 month</option>
                <option value="-3 month">3 months</option>
                <option value="-6 month">6 months</option>
                <option value="-12 month">12 months</option>
              </b-select>
              </div>
            </p>
          </header>
          <div class="card-content">
            <div class="content">
              <ALineChart :height="220" :options="realtimeOptions"/>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="columns is-desktop">
      <div class="column is-12">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">All sensors</p>
          </header>
          <div class="card-content">
            <div class="content">
              <ALineChart :height="220" :options="allSensorsOptions"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/widgets/LineChart.vue";
import ALineChart from "@/components/widgets/ALineChart.vue";
import { util } from "@/mixins/util";

export default {
  name: "Dashboards",
  components: { LineChart, ALineChart },
  mixins: [util],
  data() {
    return {
      temperatureOptions: {
        title: ["Temperature"],
        request: {
          url: "/api/data/out/random",
          data: {
            amount: 10,
            datasets: 1,
            min_value: 1,
            max_value: 20
          }
        }
      },
      humidityOptions: {
        title: ["Humidity"],
        request: {
          url: "/api/data/out/random",
          data: {
            amount: 10,
            datasets: 1,
            min_value: 1,
            max_value: 20
          }
        }
      },
      soilOptions: {
        title: ["Soil"],
        request: {
          url: "/api/data/out/random",
          data: {
            amount: 10,
            datasets: 1,
            min_value: 1,
            max_value: 20
          }
        }
      },
      allSensorsOptions: {
        title: ["Temperature", "Humidity", "Soil"],
        request: {
          url: "/api/data/out/random",
          data: {
            amount: 20,
            datasets: 3,
            min_value: 1,
            max_value: 20
          }
        }
      },
      realtimeOptions: {
        title: ["Temperature", "Humidity", "Soil"],
        request: {
          url: "/api/data/out/device",
          data: {
            device_id: 1,
            type: "temperature",
            start_dt: null,
            end_dt: null,
            format_dt: "%H:%M:%S"
          }
        },
        interval: 2000,
        moment: {
          value: "-5 minute"
        }
      }
    };
  },
  timers: {
    updateTileOptions: {
      time: 5000,
      autostart: true,
      repeat: true,
      immediate: true
    }
  },
  methods: {
    updateTileOptions() {
      // update realtime options
      this.realtimeOptions.request.data.start_dt = this.getUtcMomentFromValue(
        this.realtimeOptions.moment.value
      );

      this.realtimeOptions.request.data.end_dt = this.getUtcMomentFromValue("");

      // update others
      // ...
    },
    onRealtimeMomentChanged(value) {
      this.$timer.restart("updateTileOptions");
    }
  },
  mounted() {}
};
</script>

<style scoped>
</style>
