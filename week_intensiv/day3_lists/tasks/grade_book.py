class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self):
        self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        best_student = None
        best_average = -1
        for name, grades in self.students.items():
            if grades:
                average=sum(grades)/len(grades)
                if average > best_average:
                    best_average = average
                    best_student = name
        return best_student

