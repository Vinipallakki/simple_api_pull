import requests
import json
import csv
import time

# Constants
API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "8de3885a43c2983c713269e2b4f26ac2"  # Replace with your OpenWeatherMap API key
CITY_NAME = "London"  # Replace with your preferred city
OUTPUT_FILE = "weather_data.json"  # Local file path to save the data
CSV_FILE = "important_file.csv"  # CSV file path to save the extracted data

def fetch_weather_data(city, api_key):
    """Fetch weather data from the OpenWeatherMap API."""
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(API_URL, params=params)
    print("Request URL:", response.url)  # Debugging: See the full URL
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def save_to_local(data, file_path):
    """Save JSON data to a local file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved locally at {file_path}")

def extract_and_save_data():
    """Extract specific weather data and save it to CSV."""
    # Load the JSON data from the file
    with open(OUTPUT_FILE, 'r') as file:
        data = json.load(file)

    # Extract the desired fields
    extracted_data = {
        "id": data.get('id'),
        "temp_max": data['main'].get('temp_max'),
        "name": data.get('name'),
        "country": data['sys'].get('country')
    }

    # Write the extracted data to a CSV file
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['id', 'temp_max', 'name', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header (field names)
        writer.writeheader()
        
        # Write the data
        writer.writerow(extracted_data)

    print(f"Data has been saved to '{CSV_FILE}'")

def main():
    try:
        print("Fetching weather data...")
        data = fetch_weather_data(CITY_NAME, API_KEY)

        print("Saving data locally...")
        save_to_local(data, OUTPUT_FILE)

        print("Process completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the main program and then schedule it to run every 2 minutes
if __name__ == "__main__":
    main()
    
    # Schedule the extraction and saving of data every 2 minutes
    while True:
        extract_and_save_data()
        time.sleep(2)  # Wait for 2 minutes before running again
