jury_count = int(input())
total_average = 0
presentation_count = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    presentation_count += 1
    current_grade_sum = 0

    for _ in range(jury_count):
        grade = float(input())
        current_grade_sum += grade

    average_grade = current_grade_sum / jury_count
    total_average += average_grade

    print(f"{presentation_name} - {average_grade:.2f}.")

final_assessment = total_average / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")