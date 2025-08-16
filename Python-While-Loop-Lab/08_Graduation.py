student_name = input()
excluded_count = 0
grades_sum = 0
grade_year = 1

while grade_year <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded_count += 1
        if excluded_count > 1:
            print(f"{student_name} has been excluded at {grade_year} grade")
            break
    else:
        grades_sum += grade
        grade_year += 1
else:
    average_grade = grades_sum / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")