pages_in_current_book = int(input())
reading_pace = int(input())
days_for_reading = int(input())

all_hours = int(pages_in_current_book / reading_pace)
hours_per_day = int(all_hours / days_for_reading)

print(hours_per_day)