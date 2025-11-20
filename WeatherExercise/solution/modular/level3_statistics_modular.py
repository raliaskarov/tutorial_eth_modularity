"""
Level 3 MODULAR: Statistics Tracking (Observer Pattern)
========================================================

Adds statistics tracking to weather station.
- CurrentConditionsDisplay shows current weather
- AlertSystem monitors for warnings
- StatisticsDisplay tracks min/max/avg values
- Three independent observers working together
"""


class WeatherStation:
    """Weather data source that notifies observers of changes."""

    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def register_observer(self, observer):
        """Add an observer to the notification list."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Remove an observer from the notification list."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        """Notify all registered observers of weather changes."""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature, humidity, pressure):
        """Update weather measurements and notify observers."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay:
    """Displays current weather conditions."""

    def __init__(self, weather_station):
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
        weather_station.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """Receive weather update."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        """Display current conditions."""
        print(f"Current: {self._temperature:.1f}°C, "
              f"{self._humidity:.1f}% humidity, {self._pressure:.1f} hPa")


class AlertSystem:
    """Monitors weather conditions and sends alerts."""

    def __init__(self, weather_station, temp_min=-10.0, temp_max=35.0, pressure_min=950.0):
        self._temp_min = temp_min
        self._temp_max = temp_max
        self._pressure_min = pressure_min
        weather_station.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """Receive weather update and check for alerts."""
        # Temperature alerts
        if temperature < self._temp_min:
            print(f"🚨 COLD ALERT: Temperature {temperature:.1f}°C is below minimum!")
        elif temperature > self._temp_max:
            print(f"🚨 HEAT ALERT: Temperature {temperature:.1f}°C is above maximum!")

        # Pressure alerts
        if pressure < self._pressure_min:
            print(f"🚨 STORM ALERT: Low pressure {pressure:.1f} hPa detected!")

        # Humidity alerts
        if humidity > 90:
            print(f"🚨 HUMIDITY ALERT: Very high humidity {humidity:.1f}%!")


class StatisticsDisplay:
    """Tracks and displays weather statistics."""

    def __init__(self, weather_station):
        self._temp_readings = []
        self._humidity_readings = []
        weather_station.register_observer(self)

    def update(self, temperature, humidity, pressure):
        """Receive weather update and track statistics."""
        self._temp_readings.append(temperature)
        self._humidity_readings.append(humidity)

        # Keep only last 100 readings
        if len(self._temp_readings) > 100:
            self._temp_readings.pop(0)
            self._humidity_readings.pop(0)

        self.display()

    def display(self):
        """Display weather statistics."""
        if len(self._temp_readings) < 2:
            print("Statistics: Insufficient data")
            return

        min_temp = min(self._temp_readings)
        max_temp = max(self._temp_readings)
        avg_temp = sum(self._temp_readings) / len(self._temp_readings)

        min_hum = min(self._humidity_readings)
        max_hum = max(self._humidity_readings)
        avg_hum = sum(self._humidity_readings) / len(self._humidity_readings)

        print(f"Statistics: Temp {min_temp:.1f}-{max_temp:.1f}°C (avg {avg_temp:.1f}°C), "
              f"Humidity {min_hum:.1f}-{max_hum:.1f}% (avg {avg_hum:.1f}%)")


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    # Create and register observers
    current_display = CurrentConditionsDisplay(weather_station)
    alert_system = AlertSystem(weather_station)
    stats_display = StatisticsDisplay(weather_station)

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
