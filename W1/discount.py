from datetime import datetime

#Por mejorar debo definir constantes para el procentage descuento y el impuesto

current_date = datetime.now()

day_of_week = int(current_date.weekday())

subtotal = float(input("Subtotal without taxes: "))

if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    discount = float(subtotal * .1)
    print(f'Discount received: {discount:.2f}')
    subtotal -= discount
    
taxes = subtotal * .06
total = subtotal + taxes
print(f'Tax: {taxes:.2f}')
print(f'Total: {total:.2f}')
