import math

n = int(input())

count = 1
rows = 1
while count < n:
    count += rows + 1
    rows += 1

current_num = 1
for i in range(1, rows + 1):
    for j in range(i):
        if current_num > n:
            break
        print(current_num, end=' ')
        current_num += 1
    if current_num > n:
        break
    print()