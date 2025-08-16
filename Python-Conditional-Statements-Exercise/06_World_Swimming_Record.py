import math

world_record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())

normal_swim_time = distance_meters * time_per_meter

resistance_delay_count = math.floor(distance_meters / 15)
total_resistance_delay = resistance_delay_count * 12.5

ivan_total_time = normal_swim_time + total_resistance_delay

if ivan_total_time < world_record_seconds:
    print(f"Yes, he succeeded! The new world record is {ivan_total_time:.2f} seconds.")
else:
    seconds_slower = ivan_total_time - world_record_seconds
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")