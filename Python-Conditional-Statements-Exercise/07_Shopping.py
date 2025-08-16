budget = float(input())
num_video_cards = int(input())
num_processors = int(input())
num_ram = int(input())

video_card_price_per_unit = 250

total_video_card_cost = num_video_cards * video_card_price_per_unit

processor_price_per_unit = 0.35 * total_video_card_cost
ram_price_per_unit = 0.10 * total_video_card_cost

total_processor_cost = num_processors * processor_price_per_unit
total_ram_cost = num_ram * ram_price_per_unit

total_cost = total_video_card_cost + total_processor_cost + total_ram_cost

if num_video_cards > num_processors:
    total_cost *= 0.85

if budget >= total_cost:
    remaining_budget = budget - total_cost
    print(f"You have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")