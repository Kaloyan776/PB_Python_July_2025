budget = float(input())
season = input()

if budget <= 100:
    if season == "summer":
        print("Somewhere in Bulgaria")
        print(f"Camp - {(budget * 30 / 100):.2f}")
    elif season == "winter":
        print("Somewhere in Bulgaria")
        print(f"Hotel - {(budget * 70 / 100):.2f}")
elif budget <= 1000:
    if season == "summer":
        print("Somewhere in Balkans")
        print(f"Camp - {(budget * 40 / 100):.2f}")
    elif season == "winter":
        print("Somewhere in Balkans")
        print(f"Hotel - {(budget * 80 / 100):.2f}")
elif budget > 1000:
    if season == "summer":
        print("Somewhere in Europe")
        print(f"Hotel - {(budget * 90 / 100):.2f}")
    elif season == "winter":
        print("Somewhere in Europe")
        print(f"Hotel - {(budget * 90 / 100):.2f}")