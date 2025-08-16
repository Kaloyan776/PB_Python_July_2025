width = int(input())
length = int(input())
total_pieces = width * length
while total_pieces > 0:
    command = input()
    if command == "STOP":
        break
    pieces_taken = int(command)
    total_pieces -= pieces_taken
if total_pieces > 0:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")