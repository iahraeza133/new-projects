import datetime
import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
import requests
class DigitalClock:
    def __init__(self):
        current_time = datetime.datetime.now()
        self.hour = current_time.hour
        self.minute = current_time.minute
        self.second = current_time.second

    def show_time(self):
        return f"Time is {self.hour:02}:{self.minute:02}:{self.second:02}" 



def get_location_by_ip():
    try:
        # Use ipinfo.io API to get location data based on IP
        response = requests.get("https://ipinfo.io")
        data = response.json()

        # Extract relevant information
        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        location = data.get('loc')  

        print(f"IP Address: {ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"Coordinates: {location}")
    except Exception as e:
        print(f"Error fetching location data: {e}")

    except Exception as e:
        ip_label_var.set(f"Error: {e}")

window = tk.Tk()
window.title("IP Geolocation & Digital Clock")
window.geometry("400x300")

clock = DigitalClock()
time_label_var = tk.StringVar()
time_label_var.set(clock.show_time())

def update_time():
    clock.__init__()  # Reinitialize to update the time
    time_label_var.set(clock.show_time())
    window.after(1000, update_time)  # Updates every second

ip_label_var = tk.StringVar()
city_label_var = tk.StringVar()
region_label_var = tk.StringVar()
country_label_var = tk.StringVar()
location_label_var = tk.StringVar()

ttk.Label(window, textvariable=time_label_var).pack(pady=5)
ttk.Label(window, textvariable=ip_label_var).pack(pady=5)
ttk.Label(window, textvariable=city_label_var).pack(pady=5)
ttk.Label(window, textvariable=region_label_var).pack(pady=5)
ttk.Label(window, textvariable=country_label_var).pack(pady=5)
ttk.Label(window, textvariable=location_label_var).pack(pady=5)

fetch_button = ttk.Button(window, text="Fetch Location", command=get_location_by_ip)
fetch_button.pack(pady=20)

update_time()  # Start the clock update
window.mainloop()