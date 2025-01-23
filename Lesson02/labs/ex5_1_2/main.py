from student import Student
from school import School

s1 = Student(3)
s1.id = 1
s1.name = "Koby"
s1.addGrade(95)
s1.addGrade(100)
s1.addGrade(92)

s2 = Student(2)
s2.id = 2
s2.name = "Hodaya"
s2.addGrade(70)
s2.addGrade(80)
s2.addGrade(90)

school = School()
school.addStudent(s1)
school.addStudent(s2)
school.addStudent(s1)

school.printStudentsData()

print(s1.getAvg())
print(s2.getAvg())
