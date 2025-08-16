while True:
    destination = input()
    if destination == "End":
        break

    min_budget = float(input())
    suma = 0.00
    savings_per_save = 0.00
    while min_budget > suma:
        savings_per_save = float(input())
        suma += savings_per_save

    print(f"Going to {destination}!")