step_goal = 10000
all_steps = 0
while all_steps < step_goal:
    steps_attempt = input()
    if steps_attempt == "Going home":
        steps_to_home = int(input())
        all_steps += steps_to_home
        break
    steps_attempt_in_num = int(steps_attempt)
    all_steps += steps_attempt_in_num

if all_steps > step_goal:
    print("Goal reached! Good job!")
    print(f"{all_steps - step_goal} steps over the goal!")
else:
    print(f"{step_goal - all_steps} more steps to reach goal.")