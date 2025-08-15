import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Step 1: Use Open-Meteo's public API for New Delhi
URL = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&hourly=temperature_2m"

# ✅ Step 2: Fetch data
response = requests.get(URL)
data = response.json()

# ✅ Step 3: Extract the next 24 hours of temperature and time
times = data['hourly']['time'][:24]
temps = data['hourly']['temperature_2m'][:24]

# ✅ Step 4: Create a line graph
plt.figure(figsize=(12, 6))
sns.lineplot(x=times, y=temps, marker='o')
plt.title("Hourly Temperature Forecast - New Delhi (Next 24 Hours)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
