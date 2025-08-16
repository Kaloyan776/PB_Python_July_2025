actor_name = input()
academy_points = float(input())
judges_count = int(input())

total_points = academy_points
nomination_threshold = 1250.5

for number in range(judges_count):
    if total_points >= nomination_threshold:
        break

    judge_name = input()
    judge_points = float(input())

    points_from_judge = (len(judge_name) * judge_points) / 2
    total_points += points_from_judge

if total_points >= nomination_threshold:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = nomination_threshold - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")