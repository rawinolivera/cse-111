import datetime
import math

width1 = 185
aspect_ratio1 = 50
wheel_diameter1 = 14

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

tire_volume_liters1 = (math.pi * width1**2 * aspect_ratio1 * (width1 * aspect_ratio1 + 2540 * wheel_diameter1)) / 10000000000
with open('volumes.txt', 'a') as file:
    file.write(f"{current_date}, {width1}, {aspect_ratio1}, {wheel_diameter1}, {tire_volume_liters1:.2f} liters ")

print(f"The approximate volume is: {tire_volume_liters1:.2f} liters")


width2 = 205
aspect_ratio2 = 60
wheel_diameter2 = 15

tire_volume_liters2 = (math.pi * width2**2 * aspect_ratio2 * (width2 * aspect_ratio2 + 2540 * wheel_diameter2)) / 10000000000

with open('volumes.txt', 'a') as file:
    file.write(f"{current_date}, {width2}, {aspect_ratio2}, {wheel_diameter2}, {tire_volume_liters2:.2f} liters ")

print(f"The approximate volume is: {tire_volume_liters2:.2f} liters")
