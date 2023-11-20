# Abbas Salim
# 2026396
import csv

class Student:
    def __init__(self, studentID, studentName, major, gpa, graduationDate, disciplineReason, disciplineDate):
        self.studentID = studentID
        self.studentName = studentName
        self.major = major
        self.gpa = gpa
        self.graduationDate = graduationDate
        self.disciplineReason = disciplineReason
        self.disciplineDate = disciplineDate

    def toDict(self):
        return {
            'Student ID': self.studentID,
            'Student Name': self.studentName,
            'Major': self.major,
            'GPA': self.gpa,
            'Graduation Date': self.graduationDate
        }

def readStudentsMajors():
    studentsMajors = {}
    with open('StudentsMajorsList-3.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            studentsMajors[row['Student ID']] = row['Major']
    return studentsMajors


def readGPAs():
    gpas = {}
    with open('GPAList-1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gpas[row['Student ID']] = float(row['GPA'])
    return gpas


def readGraduationDates():
    graduationDates = {}
    with open('GraduationDatesList-1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            graduationDates[row['Student ID']] = row['Graduation Date']
    return graduationDates


def readDisciplinedStudents():
    disciplinedStudents = []
    with open('DisciplinedStudents-1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            disciplinedStudents.append(row)
    return disciplinedStudents


def writeFullRoster():
    with open('FullRoster.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Student ID', 'Student Name', 'Major', 'GPA', 'Graduation Date'])
        writer.writeheader()
        for student in students.values():
            writer.writerow(student.toDict())


def writeComputerInformationSystemsStudents():
    with open('ComputerInformationSystemsStudents.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Student ID', 'Student Name', 'Major', 'GPA', 'Graduation Date'])
        writer.writeheader()
        for student in students.values():
            if student.major == 'Computer Information Systems':
                writer.writerow(student.toDict())


def writeScholarshipCandidates():
    with open('ScholarshipCandidates.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Student ID', 'Student Name', 'Major', 'GPA', 'Graduation Date'])
        writer.writeheader()
        for student in students.values():
            if student.gpa >= 3.5:
                writer.writerow(student.toDict())


def writeDisciplinedStudents():
    with open('DisciplinedStudents.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Student ID', 'Student Name', 'Discipline Reason', 'Discipline Date'])
        writer.writeheader()
        for student in disciplinedStudents:
            writer.writerow(student)


def main():
    studentsMajors = readStudentsMajors()
    gpas = readGPAs()
    graduationDates = readGraduationDates()
    disciplinedStudents = readDisciplinedStudents()

    students = {}
    for studentID in studentsMajors.keys():
        student = Student(studentID, studentsMajors[studentID], gpas[studentID], graduationDates[studentID], None, None)
        students[studentID] = student

    for student in disciplinedStudents:
        studentID = student['Student ID']
        students[studentID].disciplineReason = student['Discipline Reason']
        students[studentID].disciplineDate = student['Discipline Date']

    writeFullRoster()
    writeComputerInformationSystemsStudents()
    writeScholarshipCandidates()
    writeDisciplinedStudents()


if __name__ == '__main__':
    main()
