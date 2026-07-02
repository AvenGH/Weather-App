import requests
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

api_key = "87a8c232e98289e9b300ff041eb611c9"

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry("500x350")
root.title("Weather App")
root.iconbitmap("C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\app_icon.ico")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text='Welcome! Please choose a location.', font=('Arial', 24))
title.pack(pady=12, padx=10)

location_entry = ctk.CTkEntry(master=frame, width=240, height=35, font=("Arial", 14), placeholder_text="Location...")
location_entry.pack(pady=10)

my_label = ctk.CTkLabel(frame, text="", image="")
my_label.pack()

label1 = ctk.CTkLabel(master=frame, text="", font=("Arial", 14))
label1.pack()

label2 = ctk.CTkLabel(master=frame, text="", font=("Arial", 14))
label2.pack()

label3 = ctk.CTkLabel(master=frame, text="", font=("Arial", 14))
label3.pack()


weather_map = {
    "Clear" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\sun.png",
    "Clouds" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\clouds.png",
    "Rain" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\rain.png",
    "Thunderstorm" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\thunder.jpg",
    "Snow" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\snow.jpeg",
    "Mist" : "C:\\Users\\avnik\\OneDrive\\Documents\\python\\Projects\\Weather App\\weather_images\\mist.png"
}


def display_weather(weather_data):
    description = weather_data['weather'][0]['description']
    temperature = round(weather_data['main']['temp'])
    feels_like = round(weather_data['main']['feels_like'])
    high = round(weather_data['main']['temp_max'])
    low = round(weather_data['main']['temp_min'])

    my_image = ""
    try:
        image_path = weather_map[weather_data['weather'][0]['main']]
        my_image = ctk.CTkImage(dark_image=Image.open(image_path), size=(50,50))
    except Exception as e:
        print(e)
        my_label.configure(image="")

    my_label.configure(image=my_image)
    label1.configure(text=f"The weather in {location.capitalize()} is {temperature} °C with {description}.")
    label2.configure(text=f"It feels like {feels_like} °C.")
    label3.configure(text=f"Today's high is {high} °C and today's low is {low} °C.")



def clear_screen():
    # Loop through all widgets and destroy them
    for widget in root.winfo_children():
        widget.destroy()


def select_location():
    global location
    location = location_entry.get()

    if location == "":
        messagebox.showerror("Error", "Please select a location.")
        return

    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    ).json()

    if weather_data['cod'] == '404':
        messagebox.showerror("Error", "Invalid Location!")
        return
    display_weather(weather_data)
    return


select_button = ctk.CTkButton(master=frame, text="Select Location", command=select_location)
select_button.pack(pady=20)

    
if __name__ == '__main__':
    root.mainloop()