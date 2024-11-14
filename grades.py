# Assigning Values
x = 1
grade_list = []
passing_counter = 0

# Program Information
print("This program displays how many students passed, the passing percentage, and the list of grades that were inputted.")
print("If the number input is below 40 or above 100, the program will exit.")
print("Type in '0' once you finish adding your inputs.")

# Main Function
while True:
    grade = int(input(f"Student Grade {x}: "))
    grade_list.append(grade)
    x += 1
    if grade == 0: # <- Triggers the confirmation to finish adding inputs for grades
        gradeInputConfirmation = str(input("Are you done? (Yes/No): "))
        if gradeInputConfirmation == "Yes":
            print("Done")
            break
        elif gradeInputConfirmation == "No":
            x -= 1
            continue
    if grade > 100 or grade < 40: # <- Invalid inputs
        print("Invalid input, please retry.")
        exit()
    if grade >= 75: # <- Counts how many have passed
        passing_counter += 1
        continue

grade_list.remove(0) # <- ensures that 0 will not appear in the grade list

passingPercent = ((passing_counter / len(grade_list)) * 100) # <- calculates the percentage of passing

# Final Display
print(f"Passing Percentage: {round(passingPercent)}%")
print(f"Passed: {(passing_counter)} / {len(grade_list)}")
print("Grades:", grade_list)