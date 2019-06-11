# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:10:16 2019

@author: hasan
"""
def get_grade(percentage):
    grade = ''
    if percentage >=80 and percentage <=100:
        grade = "Grade: A+"
    elif percentage >=70 and percentage <=79:
        grade = "Grade: A"
    elif percentage >=60 and percentage <=69:
        grade = "Grade: B"
    elif percentage >=50 and percentage <=59:
        grade = "Grade: C"
    elif percentage >=40 and percentage <=49:
        grade = "Grade: D"
    else:
        grade = "Fail"
    return grade

def get_percentage(sumMarks,totmarks):
    return (sumMarks / totmarks) * 100