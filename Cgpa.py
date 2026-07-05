print("CGPA CALCULATOR")

num = int(input("Enter the number of courses: "))

total_unit = 0
total_point = 0

for i in range(num):
    print("\nCourse", i + 1)

    unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    else:
        point = 0

    total_unit = total_unit + unit
    total_point = total_point + (unit * point)

cgpa = total_point / total_unit

print("\nTotal Course Units:", total_unit)
print("Total Grade Points:", total_point)
print("CGPA =", round(cgpa, 2))
