number_of_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
won_tournaments = 0
gained_points = 0

for _ in range(number_of_tournaments):
    tournament_stage = input()

    if tournament_stage == "W":
        total_points += 2000
        gained_points += 2000
        won_tournaments += 1
    elif tournament_stage == "F":
        total_points += 1200
        gained_points += 1200
    elif tournament_stage == "SF":
        total_points += 720
        gained_points += 720


average_points = gained_points // number_of_tournaments
won_percentage = (won_tournaments / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{won_percentage:.2f}%")