"""
Level 2 MONOLITHIC: Alert System (No Observer Pattern)
========================================================

Adding alert system to monolithic weather station.
- Display and alerts mixed in one class
- Starting to see tight coupling
- Hard to enable/disable alerts independently
"""


class WeatherStation:
    """Weather station with everything built-in."""

    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

        # Alert thresholds
        self.temp_min = -10.0
        self.temp_max = 35.0
        self.pressure_min = 950.0
        self.alerts_enabled = True

    def set_measurements(self, temperature, humidity, pressure):
        """Update weather measurements and display all."""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        # Display everything
        self._display_current()
        if self.alerts_enabled:
            self._check_alerts()

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

    def disable_alerts(self):
        """Disable alert system."""
        self.alerts_enabled = False


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    print("=== Weather Station with Alert System ===\n")

    print("--- Normal conditions ---")
    weather_station.set_measurements(22.5, 60.0, 1013.2)

    print("\n--- Warmer ---")
    weather_station.set_measurements(25.1, 65.5, 1015.8)

    print("\n--- Hot day (triggers heat alert) ---")
    weather_station.set_measurements(38.0, 45.0, 1008.0)

    print("\n--- Storm approaching (triggers storm alert) ---")
    weather_station.set_measurements(18.5, 85.0, 945.0)

    print("\n--- Very humid (triggers humidity alert) ---")
    weather_station.set_measurements(28.0, 95.0, 1010.0)

    print("\n=== Disabling Alerts ===")
    weather_station.disable_alerts()

    print("\n--- Hot day again (no alert) ---")
    weather_station.set_measurements(37.0, 50.0, 1009.0)
