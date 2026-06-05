import requests
import pandas as pd
from datetime import datetime

print("WEATHER DATA ETL PROJECT")

api_key = "65ca0e2c1e1d32dc184d749cb96204f9"

cities = ["Chennai", "Coimbatore", "Bangalore", "Hyderabad", "Mumbai"]

weather_data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_data.append({
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Data fetched successfully for {city}")

    else:
        print(f"Failed to fetch data for {city}. Status code: {response.status_code}, Response: {response.text}")

if weather_data:
    df = pd.DataFrame(weather_data)

    df.drop_duplicates(inplace=True)

    df["temperature"] = df["temperature"].round(2)
    df["feels_like"] = df["feels_like"].round(2)
    df["weather"] = df["weather"].str.title()

    print("\nCleaned Weather Data:")
    print(df)


    df.to_csv("cleaned_weather_data.csv", index=False)

    print("\nWeather data saved successfully as cleaned_weather_data.csv")
else:
    print("\nNo weather data was fetched successfully. Cannot perform transformation or load.")
