import streamlit as st
import openai
import datetime
import requests

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to interact with GPT-3.5 (or GPT-4, if you have access)
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you're using GPT-4
            prompt=prompt,
            max_tokens=150  # Adjust tokens as needed
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

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
