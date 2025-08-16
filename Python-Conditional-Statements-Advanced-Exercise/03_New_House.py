flower_type = input()
flower_count = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    if flower_count > 80:
        price = (flower_count * 5) * 90 / 100
    else:
        price = flower_count * 5
elif flower_type == "Dahlias":
    if flower_count > 90:
        price = (flower_count * 3.80) * 85 / 100
    else:
        price = flower_count * 3.80
elif flower_type == "Tulips":
    if flower_count > 80:
        price = (flower_count * 2.80) * 85 / 100
    else:
        price = flower_count * 2.80
elif flower_type == "Narcissus":
    if flower_count < 120:
        price = (flower_count * 3) * 115 / 100
    else:
        price = flower_count * 3
elif flower_type == "Gladiolus":
    if flower_count < 80:
        price = (flower_count * 2.50) * 120 / 100
    else:
        price = flower_count * 2.50

if budget >= price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - price):.2f} leva more.")