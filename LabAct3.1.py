name = input("Enter your name: ")
course = input("Enter your course (BSIT/BSCS/BSDA): ")
year_level = input("Enter your year level: ")

print("Enter your grade for the following courses:")
cc1 = int(input("Enter the grade in CC1: "))
cc2 = int(input("Enter the grade in CC2: "))
cc7 = int(input("Enter the grade in CC7: "))

grades = [cc1, cc2, cc7]

average_grade = (
        grades[0] +
        grades[1] +
        grades[2]
    ) / len(grades)

print("")
print(f'''Hello {name} of {course}-{year_level}. Here are your grades and average:
CC1 Grade: {grades[0]}
CC2 Grade: {grades[1]}
CC7 Grade: {grades[2]}
Average: {average_grade}''')