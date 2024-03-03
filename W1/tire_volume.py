from datetime import datetime
import math

width = int(input('Width (ml): '))
aspect_ratio = int(input('Aspect Ratio: '))
diameter = int(input('Diameter (in): '))

v = float((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000)
current_date = datetime.now().strftime("%Y-%m-%d")

print(f'The volumen of space inside the tire is: {v:.2f} liters\n')

with open('volumes.txt', 'a') as txt_file:
    txt_file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {v:.4}")