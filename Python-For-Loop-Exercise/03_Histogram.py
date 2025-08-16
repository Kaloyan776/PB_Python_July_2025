num_count = int(input())
nums1 = 0
nums2 = 0
nums3 = 0
nums4 = 0
nums5 = 0

for number in range (1, num_count + 1, 1):
    user_input = int(input())
    if user_input < 200:
        nums1 = nums1 + 1
    elif 200 <= user_input <= 399:
        nums2 = nums2 + 1
    elif 400 <= user_input <= 599:
        nums3 = nums3 + 1
    elif 600 <= user_input <= 799:
        nums4 = nums4 + 1
    elif user_input >= 800:
        nums5 = nums5 + 1

print(f"{(nums1 / num_count * 100):.2f}%")
print(f"{(nums2 / num_count * 100):.2f}%")
print(f"{(nums3 / num_count * 100):.2f}%")
print(f"{(nums4 / num_count * 100):.2f}%")
print(f"{(nums5 / num_count * 100):.2f}%")