# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:21:00 2019

@author: hasan
"""
import MarksheetCalculator as MC
print("Marks sheet Program using dictionary, tuple with while loop \n")
students = {}
bio = ('Student Name','Father Name','Class')
student_counter = 0
exit = False
values = ''
while exit == False:
    student_counter += 1  
    student_details = {}
    for bio_inp in range(0,len(bio)):
        ans = input(bio[bio_inp].title()+": ")
        student_details[bio[bio_inp].title()]=ans.title()
    subList = True
    subjects = {}
    while subList:
        sub = input('Input Subject: ')
        marks = int(input("Input marks obtained out of 100: "))
        if marks < 0 or marks >100:
            print('Invalid Marks given. Must be in 1-100')
            break
        subjects[sub.title()] = marks
        again = input("\nDo you want to enter more subject? [no]: ")
        if again == '' or again.lower() == 'no':
            subList = False
    student_details['Marks'] = subjects
    students['student'+str(student_counter)]=student_details
    ask = input('\nDo you want to input marks sheet record? [no]: ')
    if ask == '' or ask.lower() == 'no':
        exit = True
        print('\nData input closed. Run program again\n')
    elif ask.lower() == 'yes':
        continue
    else:
        print('\nInvalid input! Abnormal closed. Run program again\n')
        break
        
for stdkeys,stdval in students.items():
    for std_bio,bio_data in stdval.items():
        totmarks = 0
        sumMarks = 0
        percentage = 0
        if std_bio!='Marks':
            print(std_bio+" "+bio_data)
        else:
            for sub,marks in bio_data.items():
                totmarks = totmarks + 100
                sumMarks = sumMarks + marks
                print('\t'+sub+": "+str(marks))
    percentage = MC.get_percentage(sumMarks, totmarks)
    print("Total marks obtained: "+str(sumMarks)+" out of "+str(totmarks))
    print("Securing percentage at: "+str(percentage)+"%")
    grades = MC.get_grade(percentage)
    print(grades)
    print('\n')
print(students)