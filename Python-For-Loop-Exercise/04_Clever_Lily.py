Lily_age = int(input())
washing_machine = float(input())
toy_price = int(input())

toy_count = 0
money_gift = 0
money_per_year = 10
for number in range (1, Lily_age + 1, 1):
    if number % 2 == 0:
        money_gift = money_gift + money_per_year - 1
        money_per_year += 10
    else:
        toy_count += 1

money_from_toys = toy_count * toy_price

total_money = money_gift + money_from_toys

if total_money >= washing_machine:
    print(f"Yes! {(total_money - washing_machine):.2f}")
else:
    print(f"No! {abs(total_money - washing_machine):.2f}")