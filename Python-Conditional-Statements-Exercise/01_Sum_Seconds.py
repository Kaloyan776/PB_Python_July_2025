seconds1 = int(input())
seconds2 = int(input())
seconds3 = int(input())

total_seconds = seconds1 + seconds2 + seconds3

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

if remaining_seconds < 10:
    print(f"{minutes}:0{remaining_seconds}")
else:
    print(print(f"{minutes}:{remaining_seconds}"))