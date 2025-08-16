# 04. Computer Firm // SOLVED!
computer_models = int(input())
average_rating_sum = 0
comps_sold = 0
for number in range(1, computer_models + 1, 1):
    rating_and_comp_count = input()
    rating_str = rating_and_comp_count[2]
    rating_int = int(rating_str)
    comp_count = rating_and_comp_count[0]
    comp_count_2 = rating_and_comp_count[1]
    final_comp_count_str = comp_count + comp_count_2
    final_comp_count_int = int(final_comp_count_str)

    if rating_int == 2:
        average_rating_sum += 2
    elif rating_int == 3:
        comps_sold += final_comp_count_int * 0.50
        average_rating_sum += 3
    elif rating_int == 4:
        comps_sold += final_comp_count_int * 0.70
        average_rating_sum += 4
    elif rating_int == 5:
        comps_sold += final_comp_count_int * 0.85
        average_rating_sum += 5
    elif rating_int == 6:
        comps_sold += final_comp_count_int
        average_rating_sum += 6

print(f"{comps_sold:.2f}")
print(f"{(average_rating_sum / computer_models):.2f}")