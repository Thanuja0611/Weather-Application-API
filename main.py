from weather_api import get_weather
from utils import display_weather


def main():

    print("====== Weather Application ======")

    while True:

        city = input("\nEnter City Name: ")

        weather = get_weather(city)

        display_weather(weather)

        choice = input("\nSearch another city? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using the Weather Application!")
            break


if __name__ == "__main__":
    main()