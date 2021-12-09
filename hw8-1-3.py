# Author: ATN 12/9/21

def grading(student_grade):
    '''Returns the letter grade for a student's assignemnt.'''
    if (student_grade < 60):
        return("'F'")
    elif(student_grade <= 64.999):
        return("'D'")
    elif(student_grade <= 69.999):
        return("'D+'")
    elif(student_grade <= 72.999):
        return("'C-'")
    elif(student_grade <= 76.999):
        return("'C'")
    elif(student_grade <= 79.999):
        return("'C+'")
    elif(student_grade <= 82.999):
        return("'B-'")
    elif(student_grade <= 86.999):
        return("'B'")
    elif(student_grade <= 89.999):
        return("'B+'")
    elif(student_grade <= 92.999):
        return("'A-'")
    elif(student_grade <= 96.999):
        return("'A'")
    elif(student_grade <= 100):
        return("'A'")


print(grading(20) == "'F'")
print(grading(90) == "'A-'")
print(grading(75) == "'C'")
