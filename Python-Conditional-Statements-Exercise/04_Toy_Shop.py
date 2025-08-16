import math
vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
trucks = int(input())

count = puzzles + dolls + teddies + minions + trucks
sum_made_money = puzzles * 2.60 + dolls * 3 + teddies * 4.10 + minions * 8.20 + trucks * 2

if count >= 50:
    sum_made_money = sum_made_money * 75 / 100

sum_made_money = sum_made_money * 90 / 100

if sum_made_money >= vacation_price:
    print(f"Yes! {(sum_made_money - vacation_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(sum_made_money - vacation_price):.2f} lv needed.")