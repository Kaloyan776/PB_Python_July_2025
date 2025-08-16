days = int(input())
room_type = input()
review = input()

nights = days - 1

price_per_night = 0
discount = 0

if room_type == "room for one person":
    price_per_night = 18
    discount = 0
elif room_type == "apartment":
    price_per_night = 25
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif room_type == "president apartment":
    price_per_night = 35
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    else:
        discount = 0.20

total = nights * price_per_night
total -= total * discount

if review == "positive":
    total += total * 0.25
elif review == "negative":
    total -= total * 0.10

print(f"{total:.2f}")
