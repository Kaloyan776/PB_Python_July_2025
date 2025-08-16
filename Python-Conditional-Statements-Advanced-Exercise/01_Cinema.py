play_name = input()
rows = int(input())
columns = int(input())

if play_name == "Premiere":
    print(f"{(rows * columns * 12):.2f} leva")
elif play_name == "Normal":
    print(f"{(rows * columns * 7.50):.2f}")
elif play_name == "Discount":
    print(f"{(rows * columns * 5):.2f}")