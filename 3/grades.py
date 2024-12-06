mark = int(input("Enter the student's mark: "))

if 70 <= mark <=100:
    grade = 'A'
elif 60 <= mark < 70:
    grade = 'B'
elif 50 <= mark < 60:
    grade = 'C'
elif 40 <= mark < 50:
    grade = 'D'
elif 30 <= mark < 40:
    grade = 'E'
elif 20 <= mark < 30:
    grade = 'F'
else: grade = 'Invalid mark'
print(f"The grade is: {grade} ")
    
    