Here's an updated **README.md** file with a focus on the local execution of the program without using GCP:

---

# Weather Data Fetcher & CSV Generator

This project fetches weather data from the OpenWeatherMap API, processes the data, extracts the required fields, and saves the data as a CSV file locally. The program runs every 2 minutes on your local machine.

## Features

- Fetches weather data from OpenWeatherMap API.
- Extracts relevant fields like:
  - City ID
  - Max Temperature
  - City Name
  - Country Code
- Saves the extracted data in CSV format locally.
- Schedules the execution every 2 minutes using Python's `time.sleep`.

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed.
- **OpenWeatherMap API Key**: Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
- **requests Library**: Python library to send HTTP requests. You can install it using:
  
 
## Setup Instructions

### 1. Install Required Python Libraries

Ensure you have the `requests` library installed. You can install it using `pip`:



### 2. Replace the API Key

- Open the `api.py` file.
- Replace the `API_KEY` variable with your OpenWeatherMap API key.

### 3. Choose Your City

- In the same file (`api.py`), set the city name from which you want to fetch the weather data by modifying the `CITY_NAME` variable.
```

### 4. Run the Program Locally

Once the API key and city name are updated, you can run the program. The script fetches weather data, processes it, and saves the data as a CSV file locally.

To run the program, use the following command:

The program will run every 2 minutes and save the weather data to `important_file.csv`.

### 5. Program Behavior

- The program fetches the weather data from OpenWeatherMap every 2 minutes.
- It extracts the city ID, maximum temperature, city name, and country code from the weather data.
- The extracted data is saved to a CSV file called `important_file.csv` in the same directory.

## Code Overview

### 1. `fetch_weather_data()`

This function fetches weather data from the OpenWeatherMap API using the provided city and API key.

### 2. `save_to_csv()`

This function saves the extracted data as a CSV file locally.

### 3. `extract_and_save_data()`

This function fetches the weather data, processes it, and saves the relevant fields into a CSV file.

### 4. Scheduled Execution

The program uses a `while` loop and `time.sleep(120)` to execute the task every 2 minutes. The loop will continue running until you stop it manually.

## Example of Extracted Data in CSV

The CSV file will have the following structure:

This solution allows you to regularly fetch weather data from OpenWeatherMap, process it, and store it locally as a CSV file. The program runs every 2 minutes and can be stopped manually whenever needed.
