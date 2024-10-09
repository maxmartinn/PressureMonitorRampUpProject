import os
from flask import Flask, jsonify  # type: ignore
import random
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# Constants
THRESHOLD_PRESSURE = 100  # Pressure threshold

# MongoDB URI (make sure the password is secure)
db_password = "secretpassword"
uri = f"mongodb+srv://maxmartin54321:{db_password}@cluster0.4ndnf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database("pressure_data")  # Replace with your actual database name
collection = db.get_collection("readings")  # Replace with your actual collection name

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

# Simulate pressure data
def simulate_pressure_data():
    return random.uniform(0, 150)  # Simulate pressure between 0 and 150 units

# Store data in MongoDB
def store_data_online(pressure):
    data = {"pressure": pressure, "timestamp": time.time()}
    try:
        collection.insert_one(data)
        return "Data stored successfully in MongoDB."
    except Exception as e:
        return f"Error storing data in MongoDB: {e}"

@app.route('/get_pressure', methods=['GET'])
def get_pressure():
    pressure = simulate_pressure_data()
    alert = pressure > THRESHOLD_PRESSURE

    if alert:
        store_data_online(pressure)

    return jsonify({
        "pressure": pressure,
        "alert": alert
    })

if __name__ == "__main__":
    app.run(debug=True)
