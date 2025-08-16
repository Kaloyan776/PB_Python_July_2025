max_bad_grades = int(input())
last_exercise = ""
current_bad_grades = 0
exercise_count = 0
sum_of_grades = 0
check = True
while current_bad_grades < max_bad_grades:
    exercise = input()
    if exercise == "Enough":
        print(f"Average score: {(sum_of_grades / exercise_count):.2f}")
        print(f"Number of problems: {exercise_count}")
        print(f"Last problem: {last_exercise}")
        check = False
        break
    grade = int(input())
    if grade <= 4:
        current_bad_grades += 1
    sum_of_grades += grade
    exercise_count += 1
    last_exercise = exercise
if check:
    print(f"You need a break, {max_bad_grades} poor grades.")