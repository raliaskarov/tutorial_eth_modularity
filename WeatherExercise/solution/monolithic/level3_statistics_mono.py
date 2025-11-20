"""
Level 3 MONOLITHIC: Alerts + Statistics (No Observer Pattern)
==============================================================

Monolithic version with alerts and statistics combined.
- Display, alerts, and statistics all in one class
- Growing complexity and tight coupling
- Difficult to maintain and extend
"""


class WeatherStation:
    """Weather station with built-in alerts and statistics tracking."""

    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.temp_readings = []
        self.humidity_readings = []

        # Alert thresholds
        self.temp_min = -10.0
        self.temp_max = 35.0
        self.pressure_min = 950.0

    def set_measurements(self, temperature, humidity, pressure):
        """Update weather measurements and display all."""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        # Store for statistics
        self.temp_readings.append(temperature)
        self.humidity_readings.append(humidity)

        # Keep only last 100 readings
        if len(self.temp_readings) > 100:
            self.temp_readings.pop(0)
            self.humidity_readings.pop(0)

        # Display everything
        self._display_current()
        self._check_alerts()
        self._display_statistics()

    def _display_current(self):
        """Display current conditions."""
        print(f"Current: {self.temperature:.1f}°C, "
              f"{self.humidity:.1f}% humidity, {self.pressure:.1f} hPa")

    def _check_alerts(self):
        """Check for weather alerts."""
        # Temperature alerts
        if self.temperature < self.temp_min:
            print(f"🚨 COLD ALERT: Temperature {self.temperature:.1f}°C is below minimum!")
        elif self.temperature > self.temp_max:
            print(f"🚨 HEAT ALERT: Temperature {self.temperature:.1f}°C is above maximum!")

        # Pressure alerts
        if self.pressure < self.pressure_min:
            print(f"🚨 STORM ALERT: Low pressure {self.pressure:.1f} hPa detected!")

        # Humidity alerts
        if self.humidity > 90:
            print(f"🚨 HUMIDITY ALERT: Very high humidity {self.humidity:.1f}%!")

    def _display_statistics(self):
        """Display weather statistics."""
        if len(self.temp_readings) < 2:
            print("Statistics: Insufficient data")
            return

        min_temp = min(self.temp_readings)
        max_temp = max(self.temp_readings)
        avg_temp = sum(self.temp_readings) / len(self.temp_readings)

        min_hum = min(self.humidity_readings)
        max_hum = max(self.humidity_readings)
        avg_hum = sum(self.humidity_readings) / len(self.humidity_readings)

        print(f"Statistics: Temp {min_temp:.1f}-{max_temp:.1f}°C (avg {avg_temp:.1f}°C), "
              f"Humidity {min_hum:.1f}-{max_hum:.1f}% (avg {avg_hum:.1f}%)")


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    print("=== Weather Station with Alerts and Statistics ===\n")

    print("--- Normal conditions ---")
    weather_station.set_measurements(22.5, 60.0, 1013.2)

    print("\n--- Warmer ---")
    weather_station.set_measurements(25.1, 65.5, 1015.8)

    print("\n--- Hot day (triggers alert) ---")
    weather_station.set_measurements(38.0, 45.0, 1008.0)

    print("\n--- Cooler ---")
    weather_station.set_measurements(20.5, 55.0, 1010.0)

    print("\n--- Very humid (triggers alert) ---")
    weather_station.set_measurements(24.0, 95.0, 1012.0)
