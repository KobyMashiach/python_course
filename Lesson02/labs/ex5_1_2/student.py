class Student:
    def __init__(self, maxGrades):
        self.id = 0
        self.name = ""
        self.grades = []
        self.maxGrades = maxGrades

    def printData(self):
        print(f"id: {self.id}, name: {self.name}, grades: {self.grades}")

    def addGrade(self, grade):
        if len(self.grades) < self.maxGrades:
            self.grades.append(grade)

    def getAvg(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
