"""
Level 1 MONOLITHIC: Single Display (No Observer Pattern)
==========================================================

Monolithic version where weather station directly manages display.
- All logic in one place
- Tight coupling between station and display
"""


class WeatherStation:
    """Weather station with built-in display."""

    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def set_measurements(self, temperature, humidity, pressure):
        """Update weather measurements and display."""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self._display_conditions()

    def _display_conditions(self):
        """Display current conditions."""
        print(f"Current Conditions: {self.temperature:.1f}°C, "
              f"{self.humidity:.1f}% humidity, {self.pressure:.1f} hPa")


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    # Simulate weather updates
    print("=== Weather Station Starting ===\n")

    print("--- Update 1 ---")
    weather_station.set_measurements(22.5, 60.0, 1013.2)

    print("\n--- Update 2 ---")
    weather_station.set_measurements(25.1, 65.5, 1015.8)

    print("\n--- Update 3 ---")
    weather_station.set_measurements(20.0, 70.0, 1012.0)
