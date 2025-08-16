nailon = (int(input()) + 2) * 1.50
paint = (int(input()) * 110 / 100) * 14.50
thinner = int(input()) * 5.00
hours = int(input())

materials = nailon + paint+ thinner + 0.40
painters_sum = (materials * 30 / 100) * hours

final_sum = materials + painters_sum
print(final_sum)