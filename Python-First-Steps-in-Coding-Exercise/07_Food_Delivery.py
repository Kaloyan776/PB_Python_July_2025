chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegetarian_menu = int(input()) * 8.15
sum = chicken_menu + fish_menu + vegetarian_menu
dessert = sum * 20 / 100

final_sum = sum + dessert + 2.50
print(final_sum)