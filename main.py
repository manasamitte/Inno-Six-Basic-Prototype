
"""
Basic CLI prototype for:
Short-term forecast of gaseous air pollutants (Ground-level O3 and NO2)
using sample data (simulated for demonstration).

Author: [Your Name]
"""


# Note This Is The Basic Prototype For Calculating The Simulated Percentage Of The Gaseous Air Pollutants Like O3 And NO2.
import random
import time

# This Is The Sample Data (Percentage Of The Gaseous Air Pollutants) Of The Different Cities. 
city_data = {
    "delhi": {"NO2": 68, "O3": 45},
    "mumbai": {"NO2": 54, "O3": 50},
    "chennai": {"NO2": 49, "O3": 42},
    "kolkata": {"NO2": 62, "O3": 47},
    "bangalore": {"NO2": 40, "O3": 55},
    "hyderabad": {"NO2": 52, "O3": 48},
    "pune": {"NO2": 44, "O3": 46},
    "jaipur": {"NO2": 58, "O3": 43},
    "lucknow": {"NO2": 65, "O3": 41},
    "ahmedabad": {"NO2": 57, "O3": 49},
}

# Helper Functions To Devlop The Logic. 

def get_pollution(city: str):
    """
    Simulate fetching or predicting pollutant levels.
    Adds small random variation each time to mimic forecast updates.
    """
    city = city.lower().strip()
    if city not in city_data:
        return None

    base = city_data[city]
    # Simulate forecast variation
    NO2 = base["NO2"] + random.randint(-5, 5)
    O3 = base["O3"] + random.randint(-5, 5)

    # Clamp values to safe 0–100 range
    NO2 = max(0, min(100, NO2))
    O3 = max(0, min(100, O3))

    return {"NO2": NO2, "O3": O3}


def health_message(no2, o3):
    """
    Returns a short interpretation message based on pollutant values.
    """
    def interpret(value):
        if value < 30:
            return "Good 😊"
        elif value < 60:
            return "Moderate 😐"
        else:
            return "Unhealthy 😷"

    return f"NO₂: {interpret(no2)}, O₃: {interpret(o3)}"

# Main Function: 

def main():
    print()
    print()
    print("=" * 60)
    print(" 🌍 Short-Term Air Pollution Forecast Prototype ")
    print("=" * 60)
    print("Available Cities:", ", ".join(city_data.keys()).title())
    print()

    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("\nThank you for using the Air Quality CLI Prototype!")
            break

        result = get_pollution(city)
        if result is None:
            print("⚠️  City not found in our sample database. Try another.\n")
            continue

        print("\nFetching latest forecast data...")
        time.sleep(1.5)  # simulate processing delay

        no2 = result["NO2"]
        o3 = result["O3"]

        print(f"\n📍 City: {city.title()}")
        print(f"🔹 Forecasted NO₂ concentration: {no2}%")
        print(f"🔹 Forecasted O₃ concentration: {o3}%")
        print(f"💡 Air Quality Status → {health_message(no2, o3)}")
        print("-" * 60)
        print()

if __name__ == "__main__":
    main()

