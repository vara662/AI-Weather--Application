import os
import requests
import streamlit as st
from huggingface_hub import InferenceClient


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌤️",
    layout="centered"
)


# ============================================================
# APPLICATION TITLE
# ============================================================

st.title("🌤️ AI Weather Assistant")
st.write("Get current weather information for any city using AI.")


# ============================================================
# HUGGING FACE TOKEN
# ============================================================

HF_TOKEN = os.getenv("Access_Token")

if not HF_TOKEN:
    st.error("Hugging Face token is missing.")
    st.stop()


# ============================================================
# HUGGING FACE CLIENT
# ============================================================

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)


# ============================================================
# AI MODEL
# ============================================================

MODEL = "meta-llama/Llama-3.1-8B-Instruct"


# ============================================================
# WEATHER FUNCTION
# ============================================================

def get_weather(city):

    # --------------------------------------------------------
    # Find city coordinates
    # --------------------------------------------------------

    location_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city.strip(),
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    location_response.raise_for_status()

    location_data = location_response.json()

    if not location_data.get("results"):
        return None

    location = location_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    city_name = location["name"]
    country = location.get("country", "")

    # --------------------------------------------------------
    # Get current weather
    # --------------------------------------------------------

    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "wind_speed_10m,"
                "weather_code"
            ),
            "timezone": "auto"
        },
        timeout=10
    )

    weather_response.raise_for_status()

    weather_data = weather_response.json()

    current = weather_data["current"]

    return {
        "city": city_name,
        "country": country,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }


# ============================================================
# WEATHER DESCRIPTION
# ============================================================

def weather_description(code):

    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    return descriptions.get(code, "Unknown weather condition")


# ============================================================
# CITY INPUT
# ============================================================

city = st.text_input(
    "🏙️ Enter a city",
    placeholder="Example: Delhi"
)


# ============================================================
# GET WEATHER BUTTON
# ============================================================

if st.button("🌤️ Get Weather"):

    if not city.strip():
        st.warning("Please enter a city.")
        st.stop()

    with st.spinner("Getting weather information..."):

        try:

            # ------------------------------------------------
            # Get weather directly from Open-Meteo
            # ------------------------------------------------

            weather = get_weather(city)

            if weather is None:
                st.error(
                    f"Could not find the city '{city}'. "
                    "Please check the spelling and try again."
                )
                st.stop()

            condition = weather_description(
                weather["weather_code"]
            )

            # ------------------------------------------------
            # Create prompt for AI
            # ------------------------------------------------

            prompt = f"""
You are an AI weather assistant.

Give a short and clear weather report for the following location.

City: {weather["city"]}
Country: {weather["country"]}
Temperature: {weather["temperature"]} °C
Humidity: {weather["humidity"]}%
Wind Speed: {weather["wind_speed"]} km/h
Weather Condition: {condition}

Explain the weather in simple language and give one useful suggestion
for the person based on the current weather.
Do not invent any additional weather information.
"""

            # ------------------------------------------------
            # Ask Hugging Face AI
            # ------------------------------------------------

            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=200
            )

            ai_report = response.choices[0].message.content

            # ------------------------------------------------
            # Display AI report
            # ------------------------------------------------

            st.subheader("🤖 AI Weather Report")

            st.write(ai_report)

            # ------------------------------------------------
            # Display weather data
            # ------------------------------------------------

            st.subheader("📊 Current Weather")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🌡️ Temperature",
                    f"{weather['temperature']} °C"
                )

            with col2:
                st.metric(
                    "💧 Humidity",
                    f"{weather['humidity']}%"
                )

            with col3:
                st.metric(
                    "💨 Wind Speed",
                    f"{weather['wind_speed']} km/h"
                )

            st.info(
                f"Weather condition: {condition}"
            )

            st.caption(
                f"Location: {weather['city']}, {weather['country']}"
            )

        except requests.exceptions.RequestException as error:

            st.error(
                f"Weather service error: {error}"
            )

        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )