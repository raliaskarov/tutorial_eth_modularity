# Weather Station - Exercise

**Pattern**: Observer
**Goal**: Learn how Observer enables one-to-many dependencies between objects

## What We're Building
A weather monitoring system that displays current conditions and notifies multiple independent components (alerts, statistics, forecasts) when weather data changes. You'll see how the Observer pattern allows features to be added/removed without modifying the core weather station.

## Quick Start
1. Level 1 is provided as working starter code
2. Implement levels 2-4 in both `template/monolithic/` and `template/modular/`
3. Compare your solutions with `solution/` when done

---

## Level 1: Display Only

**Requirements**:
- Weather station tracks temperature, humidity, and pressure
- Display current conditions when measurements change
- Automatic updates when new data arrives

**Example**:
```
Current Conditions: 22.5°C, 60.0% humidity, 1013.2 hPa
```

**Status**: ✓ Provided as starter code

---

## Level 2: Alert System

**New Requirements**:
- Monitor for dangerous conditions
- Alert thresholds: temp < -10°C (cold), temp > 35°C (heat), pressure < 950 hPa (storm), humidity > 90% (humidity)
- Print alerts with 🚨 prefix
- Ability to enable/disable alerts

**Example**:
```
Current: 38.0°C, 45.0% humidity, 1008.0 hPa
🚨 HEAT ALERT: Temperature 38.0°C is above maximum!
```

---

## Level 3: Statistics Tracking

**New Requirements**:
- Track min/max/average for temperature and humidity
- Maintain history of last 100 readings
- Display "Insufficient data" if less than 2 readings
- Keep display and alerts from Level 2

**Example**:
```
Current: 38.0°C, 45.0% humidity, 1008.0 hPa
🚨 HEAT ALERT: Temperature 38.0°C is above maximum!
Statistics: Temp 22.5-38.0°C (avg 28.5°C), Humidity 45.0-65.5% (avg 56.8%)
```

---

## Level 4: Weather Forecast

**New Requirements**:
- Predict weather based on last 3 pressure readings
- Rising pressure → "Improving weather"
- Falling pressure → "Deteriorating weather"
- Otherwise → "Stable conditions"
- Keep all features from Level 3

**Example**:
```
Current: 18.5°C, 85.0% humidity, 945.0 hPa
🚨 STORM ALERT: Low pressure 945.0 hPa detected!
Statistics: Temp 18.5-38.0°C (avg 26.0°C), Humidity 45.0-85.0% (avg 63.9%)
Forecast: Deteriorating weather
```
