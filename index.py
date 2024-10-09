import requests
import random
import time

# Constants
THRESHOLD_PRESSURE = 100  # Define the pressure threshold
API_ENDPOINT = "https://your-database-api.com/store_data"  # Replace with your actual API endpoint

def simulate_pressure_data():
    """Simulates pressure data from a sensor."""
    return random.uniform(0, 150)  # Simulated pressure between 0 and 150 units

def alert_user(pressure):
    """Alerts the user if the pressure exceeds the threshold."""
    print(f"ALERT! Pressure exceeded: {pressure:.2f} units")

def store_data_online(pressure):
    """Stores the pressure data in an online database."""
    data = {"pressure": pressure, "timestamp": time.time()}
    try:
        response = requests.post(API_ENDPOINT, json=data)
        if response.status_code == 200:
            print("Data stored successfully.")
        else:
            print("Failed to store data.")
    except requests.RequestException as e:
        print(f"Error storing data: {e}")

def main():
    """Main function to run the pressure sensor simulation."""
    while True:
        pressure = simulate_pressure_data()
        print(f"Current Pressure: {pressure:.2f} units")

        if pressure > THRESHOLD_PRESSURE:
            alert_user(pressure)
            store_data_online(pressure)

        time.sleep(1)  # Simulate real-time data every second

if __name__ == "__main__":
    main()
