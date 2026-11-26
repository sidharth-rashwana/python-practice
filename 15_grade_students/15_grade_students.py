import math


def next_multiple_of_5(x):
    return 5 * math.ceil(x / 5)


def gradingStudents(grades):
    updated_grades = []                                             
    for grade in grades:
        if grade < 38:
            updated_grades.append(grade)
        else:
            rounded = next_multiple_of_5(grade)
            if rounded - grade < 3:
                updated_grades.append(rounded)
            else:
                                                                  
                updated_grades.append(grade)
    return updated_grades


print(gradingStudents([73, 67, 38, 33]))
