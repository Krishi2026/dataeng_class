import json
import requests

# Function to fetch bus data from the API
def fetch_bus_data(vehicle_id):
    url = f"https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id={vehicle_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for vehicle ID {vehicle_id}")
        return None

# Function to save bus data to a JSON file
def save_to_json(vehicle_ids, output_file):
    bus_data_list = []
    for vehicle_id in vehicle_ids:
        data = fetch_bus_data(vehicle_id)
        if data:
            bus_data_list.extend(data)
    with open(output_file, 'w') as f:
        json.dump(bus_data_list, f, indent=2)
    print(f"Bus data saved to {output_file}")

# Hardcoded vehicle IDs and output filename
vehicle_ids = [2910, 3504]
output_file = "bcsample.json"
save_to_json(vehicle_ids, output_file)
