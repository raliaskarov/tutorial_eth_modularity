"""
Level 2 MODULAR: Alert System (Observer Pattern)
=================================================

Adds alert monitoring to weather station.
- CurrentConditionsDisplay shows current weather
- AlertSystem monitors conditions and sends warnings
- Demonstrates multiple independent observers
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


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    # Create and register observers
    current_display = CurrentConditionsDisplay(weather_station)
    alert_system = AlertSystem(weather_station)

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
    weather_station.remove_observer(alert_system)

    print("\n--- Hot day again (no alert) ---")
    weather_station.set_measurements(37.0, 50.0, 1009.0)
