"""
HackerLand University has the following grading policy:
Every student receives a grade in the inclusive range from to 0-100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's
grade according to these rules:
    - If the difference between the grade and the next multiple of 5 
    is less than 3, round up to the next multiple of 5.
    - If the value of grade is less than 38, no rounding occurs
    as the result will still be a failing grade.

Examples:
    grade = 84 round to 85 (85 - 84 is less than 3)
    grade = 29 do not round (result is less than 40)
    grade = 57 do not round (60 - 57 is 3 or higher) 

Given the initial grade for each of Sam's n students, write code to automate the rounding process. 
"""

def roundToUpper5(num):   
    num2 = 5 * int(num/5)
    if num2 < num:
        num2+=5
    return num2



def gradingStudents(grades):
    # Write your code here
    newGrades=[]
    for g in grades:
        if g < 38:
            newGrades.append(g)
            continue
        g2 = roundToUpper5(g)
        if (g2 - g) < 3:
            newGrades.append(g2)
        else:
            newGrades.append(g)
    return newGrades
    pass

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

"""
4
73
67
38
33
"""