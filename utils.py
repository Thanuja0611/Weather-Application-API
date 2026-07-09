def display_weather(weather):

    if "error" in weather:
        print("\nError:", weather["error"])
        return

    print("\n========== Weather Report ==========")
    print(f"City        : {weather['city']}")
    print(f"Temperature : {weather['temperature']} °C")
    print(f"Humidity    : {weather['humidity']} %")
    print(f"Wind Speed  : {weather['wind_speed']} m/s")
    print(f"Condition   : {weather['condition']}")
    print("====================================")