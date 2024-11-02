import requests
from tkinter import *
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data.get("cod") != 200:
        messagebox.showerror("Error", weather_data.get("message"))
        return

    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather_description = weather_data["weather"][0]["description"]

    location_label['text'] = f"Weather in {city}:"
    temperature_label['text'] = f"Temperature: {temperature}°C"
    weather_label['text'] = f"Condition: {weather_description.capitalize()}"

def search():
    city = city_text.get()
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

# Main application
api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

app = Tk()
app.title("Weather App")
app.geometry("300x300")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather", command=search)
search_btn.pack()

location_label = Label(app, text="Location", font=('bold', 20))
location_label.pack()

temperature_label = Label(app, text="")
temperature_label.pack()

weather_label = Label(app, text="")
weather_label.pack()

app.mainloop()