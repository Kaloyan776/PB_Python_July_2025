budget = float(input())
num_extras = int(input())
clothing_price_per_extra = float(input())

decor_cost = budget * 0.10

total_clothing_cost = num_extras * clothing_price_per_extra

if num_extras > 150:
    total_clothing_cost *= 0.90

total_expenses = decor_cost + total_clothing_cost

if total_expenses > budget:
    needed_money = total_expenses - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    money_left = budget - total_expenses
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")