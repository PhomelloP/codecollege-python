from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Read the CSV file
path = Path('weather data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])  # Use float for more precise values
    dates.append(current_date)
    rainfall.append(rain)

# Print header row for reference
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Plot the rainfall
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='red')

# Format plot
ax.set_title("Sitka Rainfall, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Rainfall (ml)", fontsize=16)  # Make sure the unit is correct
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.show()
