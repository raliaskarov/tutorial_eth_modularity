# weather_mono.py
# record mesurements of temp hum pressure

class WeatherStation:

    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.temperature_readings = []
        self.humidity_readings = []
        self.pressure_readings = []
        self.temperature_max = 0
        self.temperature_min = 0
        self.temperature_avg = 0
        self.humidity_max = 0
        self.humidity_min = 0
        self.humidity_avg = 0


    def record_measurement(self, t, h ,p):
        self.temperature = t
        self.humidity = h
        self.pressure = p

        self.temperature_readings.append(t)
        self.humidity_readings.append(h)
        self.pressure_readings.append(p)

        if len(self.temperature_readings) < 2:
            print("Temperature stats - Insufficient data. Stistics skipped")
        else:
            self.temperature_max = max(self.temperature_readings)
            self.temperature_min = min(self.temperature_readings)
            self.temperature_avg = sum(self.temperature_readings) / len(self.temperature_readings)
        if len(self.humidity_readings) <2:
            print("Humidity stats - Insufficient data. Stistics skipped")
        else:
            self.humidity_max = max(self.humidity_readings)
            self.humidity_min = min(self.humidity_readings)
            self.humidity_avg = sum(self.humidity_readings) / len(self.humidity_readings)

        # display alerts
        self._display_measurements()
        self._check_alerts()
        self._display_statistics()
        self._display_forecast()

    def _check_alerts(self):
        t = self.temperature
        h = self.humidity
        p = self.pressure

        if t > 35:
            print(f"HEATWAVE ALERT - {t}")
            if t >= max(self.temperature_readings[:-1]):
                print(f"New temperature record!")
        if t < -10:
            print(f"COLD ALERT")
        if h > 90:
            print(f"HUMIDITY ALERT - {h}")
        if p < 950:
            print(f"THUNDERSTORM ALERT {p}")

        

    def _display_measurements(self):
        print(
            f"T : {self.temperature}\n"
            f"H : {self.humidity}\n"
            f"P : {self.pressure}\n"
            )
    
    def _display_readings(self):
        print(
            f"T_hist: {self.temperature_readings}\n"
            f"H_hist: {self.humidity_readings}\n"
            f"P_hist: {self.pressure_readings}\n"
            )

    def _display_statistics(self):
        print(
            f"T_max: {self.temperature_max} | "
            f"T_avg: {self.temperature_avg} | "
            f"T_min: {self.temperature_min}\n"
            f"H_max: {self.humidity_max} | "
            f"H_avg: {self.humidity_avg} | "
            f"H_min: {self.humidity_min}\n"
        )

    def _display_forecast(self):
        """Display weather forecast."""
        if len(self.pressure_readings) < 3:
            forecast = "Insufficient data"
        else:
            recent = self.pressure_readings
            if recent[-1] > recent[-2] > recent[-3]:
                forecast = "Improving weather"
            elif recent[-1] < recent[-2] < recent[-3]:
                forecast = "Deteriorating weather"
            else:
                forecast = "Stable conditions"
        print(f"Forecast: {forecast}")

if __name__ == "__main__":
    weather_station = WeatherStation()
    weather_station.record_measurement(t=30, h=60, p=1060)
    weather_station.record_measurement(t=38, h=60, p=1060)
    weather_station.record_measurement(t=38, h=95, p=960)
    weather_station.record_measurement(t=38, h=95, p=900)
    weather_station.record_measurement(t=28, h=80, p=1000)
