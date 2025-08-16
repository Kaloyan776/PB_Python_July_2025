n = int(input())
maxi = -9999999999999999999999999999999999999
mini = 9999999999999999999999999999999999999

for number in range(1, n + 1, 1):
    num = int(input())
    if num > maxi:
        maxi = num
    if num < mini:
        mini = num
print(f"Max number: {maxi}")
print(f"Min number: {mini}")