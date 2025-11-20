"""
Level 1 MODULAR: Single Observer (Observer Pattern Introduction)
=================================================================

Introduction to Observer pattern with a simple weather station and one display.
- WeatherStation notifies observers when data changes
- CurrentConditionsDisplay observes weather changes
- No abstract classes - using duck typing
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
        print(f"Current Conditions: {self._temperature:.1f}°C, "
              f"{self._humidity:.1f}% humidity, {self._pressure:.1f} hPa")


if __name__ == "__main__":
    # Create weather station
    weather_station = WeatherStation()

    # Create and register display
    current_display = CurrentConditionsDisplay(weather_station)

    # Simulate weather updates
    print("=== Weather Station Starting ===\n")

    print("--- Update 1 ---")
    weather_station.set_measurements(22.5, 60.0, 1013.2)

    print("\n--- Update 2 ---")
    weather_station.set_measurements(25.1, 65.5, 1015.8)

    print("\n--- Update 3 ---")
    weather_station.set_measurements(20.0, 70.0, 1012.0)
