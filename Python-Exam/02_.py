# 02. Deer of Santa // SOLVED!
import math
days_of_absence = int(input())
food_in_kilos = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

first_deer_food_needs = days_of_absence * first_deer_food_per_day
second_deer_food_needs = days_of_absence * second_deer_food_per_day
third_deer_food_needs = days_of_absence * third_deer_food_per_day
sum_of_eaten_food = first_deer_food_needs + second_deer_food_needs + third_deer_food_needs

if sum_of_eaten_food <= food_in_kilos:
    print(f"{math.floor(food_in_kilos - sum_of_eaten_food)} kilos of food left.")
else:
    print(f"{math.ceil(abs(food_in_kilos - sum_of_eaten_food))} more kilos of food are needed.")