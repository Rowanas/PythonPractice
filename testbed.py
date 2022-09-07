# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:39:06 2020

@author: Rowanas
"""

class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

#    def customStudentDecoder(self, studentDict):
#        return namedtuple("x",studentDict.keys())(studentDict.values())

student = Student("Julian", 23, ["Italian"])

# with open("./students.txt", "a") as studentslist:
#     studentslist.write("\n")
#     studentslist.close

# with open("./students.txt", "r") as studentslist:
#     students = [Student(**d) for d in json.load(studentslist)]
#     print(students)
#     studentslist.close

with open("./students.txt", "w") as studentslist:
    studentslist.write(str(student.__dict__))
    studentslist.write("\n")
    studentslist.close

with open("./students.txt", "r") as studentslist:
    studentslist.readlines()
    for line in studentslist:
        line = Student
        print(line)
        studentslist.close
#code above is reading an empty dict.


student_list = []

student_list.append(Student("John", 21, ["Maths","Drama"])),
student_list.append(Student("James", 21, ["Drama", "English"])),
student_list.append(Student("Jemima", 21, ["Spanish"])),
student_list.append(Student("Jezebel", 21, ["Science","Drama"])),

for obj in student_list:
    print (obj.courses[-1])



#studObj = json.loads(studentslist, object_hook=StudentEncoder.customStudentDecoder)
#print(studObj.courses)
