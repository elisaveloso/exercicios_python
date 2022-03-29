grade1 = int(input("What grade did you get on the first exam? "))
grade2 = int(input("What grade did you get on the second exam? "))

average = (grade1 + grade2)/2

if(average < 6):
    print("Failed")
else:
    print("Approved")
