group_budget = int(input())
season = input()
fishermen_count = int(input())
ship_rent_money = 0

if season == "Spring":
    ship_rent_money = 3000
    if fishermen_count <= 6:
        ship_rent_money = ship_rent_money - ship_rent_money * 10 / 100
    elif 7 <= fishermen_count <= 11:
        ship_rent_money = ship_rent_money - ship_rent_money * 15 / 100
    elif fishermen_count >= 12:
        ship_rent_money = ship_rent_money - ship_rent_money * 25 / 100
    if fishermen_count % 2 == 0:
        ship_rent_money = ship_rent_money - ship_rent_money * 5 / 100
elif season == "Summer":
    ship_rent_money = 4200
    if fishermen_count <= 6:
        ship_rent_money = ship_rent_money - ship_rent_money * 10 / 100
    elif 7 <= fishermen_count <= 11:
        ship_rent_money = ship_rent_money - ship_rent_money * 15 / 100
    elif fishermen_count >= 12:
        ship_rent_money = ship_rent_money - ship_rent_money * 25 / 100
    if fishermen_count % 2 == 0:
        ship_rent_money = ship_rent_money - ship_rent_money * 5 / 100
elif season == "Autumn":
    ship_rent_money = 4200
    if fishermen_count <= 6:
        ship_rent_money = ship_rent_money - ship_rent_money * 10 / 100
    elif 7 <= fishermen_count <= 11:
        ship_rent_money = ship_rent_money - ship_rent_money * 15 / 100
    elif fishermen_count >= 12:
        ship_rent_money = ship_rent_money - ship_rent_money * 25 / 100
elif season == "Winter":
    ship_rent_money = 2600
    if fishermen_count <= 6:
        ship_rent_money = ship_rent_money - ship_rent_money * 10 / 100
    elif 7 <= fishermen_count <= 11:
        ship_rent_money = ship_rent_money - ship_rent_money * 15 / 100
    elif fishermen_count >= 12:
        ship_rent_money = ship_rent_money - ship_rent_money * 25 / 100
    if fishermen_count % 2 == 0:
        ship_rent_money = ship_rent_money - ship_rent_money * 5 / 100

if group_budget >= ship_rent_money:
    print(f"Yes! You have {(group_budget - ship_rent_money):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(group_budget - ship_rent_money):.2f} leva.")