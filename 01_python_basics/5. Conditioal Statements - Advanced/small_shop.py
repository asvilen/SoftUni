product = input()
city = input()
quantity = float(input())

if product == 'coffee':
    if city == 'Sofia':
        price =  0.5
    if city == 'Plovdiv':
        price = 0.4
    if city == 'Varna':
        price = 0.45
if product == 'water':
    if city == 'Sofia':
        price = 0.8
    if city == 'Plovdiv':
        price = 0.7
    if city == 'Varna':
        price = 0.7
if product == 'beer':
    if city == 'Sofia':
        price = 1.2
    if city == 'Plovdiv':
        price = 1.15
    if city == 'Varna':
        price = 1.1
if product == 'sweets':
    if city == 'Sofia':
        price = 1.45
    if city == 'Plovdiv':
        price = 1.3
    if city == 'Varna':
        price = 1.35
if product == 'peanuts':
    if city == 'Sofia':
        price = 1.6
    if city == 'Plovdiv':
        price = 1.5
    if city == 'Varna':
        price = 1.55

total = price * quantity

print(f"{total}")