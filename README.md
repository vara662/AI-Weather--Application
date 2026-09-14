
# AI Weather Assistant

## Project Overview

AI Weather Assistant is a Streamlit-based weather application that provides current weather information for cities and regional weather summaries. The application combines the Open-Meteo weather API with a Hugging Face language model to retrieve real-time weather data and generate easy-to-understand AI-based weather reports.

The application supports individual city searches as well as state-level weather analysis. For example, users can search for cities such as Delhi, Mumbai, Chennai, or Hyderabad. Users can also enter Andhra Pradesh to view weather conditions across multiple major cities in the state.

## Features

- Search for the current weather of any city.
- Retrieve real-time temperature, humidity, and wind speed.
- Display the current weather condition.
- Generate AI-based weather explanations using Hugging Face.
- Provide state-wide weather information for Andhra Pradesh.
- Compare weather conditions across multiple major cities.
- Generate an AI summary based on the collected regional weather data.
- Simple and interactive Streamlit interface.
- Uses external APIs for live weather information.

## Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- Llama 3.1 8B Instruct
- Open-Meteo API
- Requests
- Hugging Face Hub

## Project Structure

```text
AI-Weather-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
````

## How the Application Works

The application follows a simple workflow:

1. The user enters a city or state name.
2. The application checks whether the input is an individual city or a supported state.
3. For a city, Open-Meteo's geocoding service identifies the location coordinates.
4. The Open-Meteo weather service retrieves the current weather information.
5. The collected weather data includes:

   * Temperature
   * Relative humidity
   * Wind speed
   * Weather condition
6. The weather information is passed to the Hugging Face Llama model.
7. The AI model generates a readable weather report.
8. For Andhra Pradesh, the application collects weather data from multiple major cities.
9. The collected regional information is provided to the AI model to generate a state-wide summary.

## Supported Andhra Pradesh Weather Analysis

When the user enters `Andhra Pradesh`, the application retrieves weather information from major cities including:

* Visakhapatnam
* Vijayawada
* Guntur
* Tirupati
* Nellore
* Kurnool
* Rajahmundry
* Kadapa
* Anantapur

The application then displays the weather conditions for each city and generates an overall AI-based summary.

## Requirements

Make sure Python is installed on your system.

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Hugging Face Token Setup

The application requires a Hugging Face access token for the AI-generated weather report.

Create a Hugging Face token with permission to use Inference Providers.

Do not place the token directly inside `app.py`.

### Windows PowerShell

Set the token using:

```powershell
$env:Access_Token="YOUR_HUGGING_FACE_TOKEN"
```

Replace `YOUR_HUGGING_FACE_TOKEN` with your actual token.

Never upload or publish your Hugging Face token on GitHub.

## Running the Application

Open the project folder in the terminal and run:

```bash
python -m streamlit run app.py
```

After starting the application, Streamlit will provide a local address such as:

```text
http://localhost:8501
```

Open the address in a web browser.

## Example Usage

### City Weather

Enter:

```text
Delhi
```

The application displays:

* Current temperature
* Humidity
* Wind speed
* Weather condition
* AI-generated weather report

Other examples:

```text
Mumbai
Chennai
Hyderabad
Bangalore
Kolkata
```

### State Weather

Enter:

```text
Andhra Pradesh
```

The application retrieves weather information from multiple major cities and provides an AI-generated regional summary.

## API Services

### Open-Meteo

Open-Meteo is used for:

* City geocoding
* Latitude and longitude retrieval
* Current weather information

### Hugging Face

Hugging Face Inference API is used to:

* Process the collected weather information
* Generate natural-language weather reports
* Produce regional weather summaries

## Security

The Hugging Face access token must be kept private.

Do not:

* Hardcode the token in `app.py`
* Commit the token to GitHub
* Include the token in screenshots
* Share the token publicly

Use an environment variable instead:

```powershell
$env:Access_Token="YOUR_HUGGING_FACE_TOKEN"
```

## Future Improvements

Possible improvements for future versions include:

* Seven-day weather forecasts
* Hourly weather information
* Weather maps
* Rain probability
* Air quality information
* Weather alerts
* Support for additional states and regions
* Automatic location detection
* Weather history and data visualization
* Improved AI-generated recommendations

## Author

**Varalakshmi K**

## License

This project is developed for educational and demonstration purposes.

```
```
