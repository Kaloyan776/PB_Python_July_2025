n =int(input())

for number in range(0, n + 1, 1):
    if number == 0 or number % 2 == 0:
        print(2 ** number)