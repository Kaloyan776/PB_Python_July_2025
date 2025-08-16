# 03. Excursion Calculator // SOLVED!
people_group = int(input())
season = input()
suma = 0

if people_group <= 5:
    if season == "spring":
        suma = people_group * 50
        print(f"{suma:.2f} leva.")
    elif season == "summer":
        suma = (people_group * 48.50) * 0.85
        print(f"{suma:.2f} leva.")
    elif season == "autumn":
        suma = people_group * 60
        print(f"{suma:.2f} leva.")
    elif season == "winter":
        suma = (people_group * 86) * 1.08
        print(f"{suma:.2f} leva.")
else:
    if season == "spring":
        suma = people_group * 48
        print(f"{suma:.2f} leva.")
    elif season == "summer":
        suma = (people_group * 45) * 0.85
        print(f"{suma:.2f} leva.")
    elif season == "autumn":
        suma = people_group * 49.50
        print(f"{suma:.2f} leva.")
    elif season == "winter":
        suma = (people_group * 85) * 1.08
        print(f"{suma:.2f} leva.")