import streamlit as st
import openai
import datetime
import requests

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_weather(city="London"):
    key = st.secrets["WEATHER_API_KEY"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    res = requests.get(url).json()
    weather = res["weather"][0]["description"]
    temp = res["main"]["temp"]
    return f"The weather in {city} is {weather}, {temp}°C."

def get_time():
    return datetime.datetime.now().strftime("Time: %H:%M:%S")

def handle_command(command):
    if "weather" in command:
        return get_weather()
    elif "time" in command:
        return get_time()
    else:
        return get_gpt_response(command)

st.title("JARVIS AI Assistant")
query = st.text_input("Ask me something:")

if query:
    result = handle_command(query.lower())
    st.write(result)
