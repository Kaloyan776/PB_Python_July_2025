vacation_cost = float(input())
available_money = float(input())
days_counter = 0
spend_counter = 0
while available_money < vacation_cost and spend_counter < 5:
    action = input()
    amount = float(input())
    days_counter += 1
    if action == "save":
        available_money += amount
        spend_counter = 0
    elif action == "spend":
        available_money -= amount
        spend_counter += 1
        if available_money < 0:
            available_money = 0
if spend_counter == 5:
    print("You can't save the money.")
    print(days_counter)
if available_money >= vacation_cost:
    print(f"You saved the money for {days_counter} days.")