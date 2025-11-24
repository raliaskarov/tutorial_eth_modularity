# record mesurements of temp hum pressure

class WeatherStation:

    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def record_measurement(self, t, h ,p):
        self.temperature = t
        self.humidity = h
        self.pressure = p

        if t > 35:
            print(f"HEATWAVE ALERT - {t}")
        if t < -10:
            print(f"COLD ALERT")
        if p < 900:
            print(f"THUNDERSTORM ALERT {p}")

    def display(self):
        print(
            f"T : {self.temperature}\n"
            f"H : {self.humidity}\n"
            f"P : {self.pressure}\n"
            )

class Displayer:

    def update(self, temp, hum, pres):
        print(
            f"T : {temp}"
            f"H : {hum}"
            f"P : {pres}"
        )

class Alert:
    