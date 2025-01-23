class School:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        arr = list(filter(lambda x: x.id == student.id, self.students))
        if len(arr) == 0:
            self.students.append(student)
        else:
            print("Student already registered!")

    def printStudentsData(self):
        for s in self.students:
            s.printData()
