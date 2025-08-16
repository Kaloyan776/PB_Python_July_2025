import math
name_of_series = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

time_for_episode = break_duration - lunch_time - relax_time

if time_for_episode >= episode_duration:
    print(f"You have enough time to watch {name_of_series} and left with {math.ceil(time_for_episode - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(abs(time_for_episode - episode_duration))} more minutes.")