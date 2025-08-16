# 01. Excursion // SOLVED!
people_in_group = int(input())
nights = int(input())
cards_transportation = int(input())
museum_tickets = int(input())
nights_price = nights * 20
cards_transportation_price = cards_transportation * 1.60
museum_tickets_price = museum_tickets * 6

suma = nights_price + cards_transportation_price + museum_tickets_price
group_sum = (suma * people_in_group) * 1.25

print(f"{group_sum:.2f}")