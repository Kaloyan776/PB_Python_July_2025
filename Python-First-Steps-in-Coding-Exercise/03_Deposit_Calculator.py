deposit_sum = float(input())
months = int(input())
percentage = float(input()) / 100

final_sum = deposit_sum + months * ((deposit_sum * percentage) / 12)

print(final_sum)