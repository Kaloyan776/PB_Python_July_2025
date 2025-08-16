prime_sum = 0
non_prime_sum = 0

while True:
    command = input()
    if command == "stop":
        break

    number = int(command)

    if number < 0:
        print("Number is negative.")
        continue

    if number <= 1:
        non_prime_sum += number
        continue

    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")