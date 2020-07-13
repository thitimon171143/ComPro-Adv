class StudentGPA:
    def __init__(self,name,grade1,unit1,grade2,unit2,grade3,unit3,grade4,unit4):
        if type(grade1) == str :
            if grade1 == 'A':
                grade1 = 4
            elif grade1 == 'B+':
                grade1 = 3.5
            elif grade1 == 'B':
                grade1 = 3
            elif grade1 == 'C+':
                grade1 = 2.5
            elif grade1 == 'C':
                grade1 = 2
            elif grade1 == 'D+':
                grade1 = 1.5
            elif grade1 == 'D':
                grade1 = 1
            elif grade1 == 'F':
                grade1 = 0
        if type(grade2) == str :
            if grade2 == 'A':
                grade2 = 4
            elif grade2 == 'B+':
                grade2 = 3.5
            elif grade2 == 'B':
                grade2 = 3
            elif grade2 == 'C+':
                grade2 = 2.5
            elif grade2 == 'C':
                grade2 = 2
            elif grade2 == 'D+':
                grade2 = 1.5
            elif grade2 == 'D':
                grade2 = 1
            elif grade2 == 'F':
                grade2 = 0
        if type(grade3) == str :
            if grade3 == 'A':
                grade3 = 4
            elif grade3 == 'B+':
                grade3 = 3.5
            elif grade3 == 'B':
                grade3 = 3
            elif grade3 == 'C+':
                grade3 = 2.5
            elif grade3 == 'C':
                grade3 = 2
            elif grade3 == 'D+':
                grade3 = 1.5
            elif grade3 == 'D':
                grade3 = 1
            elif grade3 == 'F':
                grade3 = 0
        if type(grade4) == str :
            if grade4 == 'A':
                grade4 = 4
            elif grade4 == 'B+':
                grade4 = 3.5
            elif grade4 == 'B':
                grade4 = 3
            elif grade4 == 'C+':
                grade4 = 2.5
            elif grade4 == 'C':
                grade4 = 2
            elif grade4 == 'D+':
                grade4 = 1.5
            elif grade4 == 'D':
                grade4 = 1
            elif grade4 == 'F':
                grade4 = 0
        self.name = name
        self.grade1 = grade1
        self.unit1 = unit1
        self.grade2 = grade2
        self.unit2 = unit2
        self.grade3 = grade3
        self.unit3 = unit3
        self.grade4 = grade4
        self.unit4 = unit4
    def sumGPA(self):
        return round(((self.grade1*self.unit1)+(self.grade2*self.unit2)+(self.grade3*self.unit3)+(self.grade4*self.unit4))
        /(self.unit1+self.unit2+self.unit3+self.unit4),2)
    def __str__(self):
        return 'Name : {} , GPA : {}'.format(self.name,self.sumGPA())
gpa_grade = StudentGPA('Fast','C+',3,'D+',1,'B',3,'C',3)
#print(gpa_grade.name,gpa_grade.sumGPA())
print(gpa_grade)