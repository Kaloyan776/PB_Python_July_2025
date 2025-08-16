width = int(input())
height = int(input())
length = int(input())
volume = width * height * length
check = True

while volume > 0:
    command = input()
    if command == "Done":
        print(f"{volume} Cubic meters left.")
        check = False
        break
    box_volume = int(command)
    volume -= box_volume

if check:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")