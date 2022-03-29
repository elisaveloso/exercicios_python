grade1 = float(input("What grade did you get on the first exam? "))
grade2 = float(input("What grade did you get on the second exam? "))

average = (grade1 + grade2)/2

concept = {"aprovado": 'Approved', "exame": 'Exam', "reprovado": 'Failed'}

if(average >= 6):
    final_grade = concept["aprovado"]
    print(final_grade)

elif(average < 6) and (average > 4):
    final_grade = concept["exame"]
    print(final_grade)

elif(average <= 4):
    final_grade = concept["reprovado"]
    print(final_grade)
