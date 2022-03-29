somatory = 0
students = 0
# while students < 10:
#     grade_request = float(input("Insert the student's grade: "))
#     if grade_request >= 0:
#         somatory = somatory + grade_request
#         students = students + 1
#     else:
#         grade_request = float(input("Insert a valid student's grade: "))

for x in range(1, 11):
    grade = float(input("Type the grade "+str(x)+": "))
    somatory = somatory + grade

print("The average of grades is:", somatory/10)
