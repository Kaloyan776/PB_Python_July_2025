# 05. Best Player // SOLVED!
max_goals = -9999999999999999999999
hat_trick_requirement = False
best_player = " "
while True:
    player_name = input()
    if player_name == "END":
        break
    scored_goals = int(input())
    if scored_goals > max_goals:
        max_goals = scored_goals
        best_player = player_name
    if scored_goals >= 3:
        hat_trick_requirement = True
    if scored_goals >= 10:
        break

if hat_trick_requirement:
    print(f"{best_player} is the best player!")
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {max_goals} goals.")