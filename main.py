import math

while True:
    try:
        kod = int(input("Выберете задание или выберете 0 для выхода: "))
        match kod:
            case 1:
                class Square:
                    def __init__(self, side):
                        self.side = side

                    def calculate_perimeter(self):
                        return 4 * self.side

                    def calculate_area(self):
                        return self.side ** 2

                    def calculate_diagonal(self):
                        return math.sqrt(2) * self.side


                while True:
                    try:
                        a = float(input("Введите значение стороны квадрата: "))
                        break
                    except ValueError:
                        print("Необходимо ввести число")
                square = Square(a)
                perimeter = square.calculate_perimeter()
                print("Периметр квадрата:", perimeter)

                area = round(square.calculate_area(), 2)
                print("Площадь квадрата:", area)

                diagonal = round(square.calculate_diagonal(), 2)
                print("Диагональ квадрата:", diagonal)
            case 2:
                class Stationery:
                    def __init__(self, title):
                        self.title = title

                    def draw(self):
                        print("Рисуем")


                class Pen(Stationery):
                    def draw(self):
                        print("Рисуем ручкой")


                class Pencil(Stationery):
                    def draw(self):
                        print("Рисуем карандашом")


                class Handle(Stationery):
                    def draw(self):
                        print("Рисуем маркером")


                pen = Pen("Ручка")
                print(f'{pen.title}:')
                pen.draw()
                pencil = Pencil("Карандаш")
                print(f'{pencil.title}:')
                pencil.draw()
                handle = Handle("Маркер")
                print(f'{handle.title}:')
                handle.draw()
            case 3:
                class Faculty:
                    def __init__(self, name):
                        self.name = name

                    def get_name(self):
                        return self.name

                    def set_name(self, name):
                        self.name = name

                def input_faculty_data():
                    faculties = []
                    while True:
                        name = input("Введите название факультета (или '0' для выхода): ")
                        if name == '0':
                            break

                        faculty = Faculty(name)
                        faculties.append(faculty)

                    return faculties


                def print_faculties(faculties):
                    for faculty in faculties:
                        print(faculty.get_name())

                def change_faculty_data(faculty):
                    name = input("Введите новое название факультета: ")

                    faculty.set_name(name)
                    print("Название факультета успешно изменено.")

                class Student:
                    def __init__(self, full_name, birth_year, exam_scores):
                        self.full_name = full_name
                        self.birth_year = birth_year
                        self.exam_scores = exam_scores

                    def get_full_name(self):
                        return self.full_name

                    def get_birth_year(self):
                        return self.birth_year

                    def get_exam_scores(self):
                        return self.exam_scores

                    def set_full_name(self, full_name):
                        self.full_name = full_name

                    def set_birth_year(self, birth_year):
                        self.birth_year = birth_year

                    def set_exam_scores(self, exam_scores):
                        self.exam_scores = exam_scores


                def input_student_data():
                    students = []
                    while True:
                        full_name = input("Введите Ф.И.О. студента (или '0' для выхода): ")
                        if full_name == '0':
                            break
                        while True:
                            try:
                                birth_year = int(input("Введите год рождения студента: "))
                                if birth_year > 0:
                                    break
                                else:
                                    print("Неправильно введен год")
                            except ValueError:
                                print("Неправильно введен год")
                        while True:
                            try:
                                exam_scores = input(
                                    "Введите результаты сдачи последней сессии (через пробел): ").split()
                                exam_scores = [int(score) for score in exam_scores]
                                if all(0 < score < 10 for score in exam_scores):
                                    break
                                else:
                                    print("Неправильно введены отметки")
                            except ValueError:
                                print("Неправильно введены отметки")

                        student = Student(full_name, birth_year, exam_scores)
                        students.append(student)

                    return students


                def print_student_performance(students):
                    for student in students:
                        print(f"Студент: {student.get_full_name()}")
                        print(f"Год рождения: {student.get_birth_year()}")
                        print(f"Результаты сдачи последней сессии: {student.get_exam_scores()}")
                        print(f"Средний балл: {round(sum(student.get_exam_scores()) / len(student.get_exam_scores()), 2)}")
                        print()


                def change_student_data(student):
                    print("Введите новые данные для студента:")
                    full_name = input("Ф.И.О.: ")
                    while True:
                        try:
                            birth_year = int(input("Введите год рождения студента: "))
                            if birth_year > 0:
                                break
                            else:
                                print("Неправильно введен год")
                        except ValueError:
                            print("Неправильно введен год")
                    while True:
                        try:
                            exam_scores = input(
                                "Введите результаты сдачи последней сессии (через пробел): ").split()
                            exam_scores = [int(score) for score in exam_scores]
                            if all(0 < score < 10 for score in exam_scores):
                                break
                            else:
                                print("Неправильно введены отметки")
                        except ValueError:
                            print("Неправильно введены отметки")

                    student.set_full_name(full_name)
                    student.set_birth_year(birth_year)
                    student.set_exam_scores(exam_scores)

                    print("Данные студента успешно изменены.")

                faculties = []
                students = []
                while True:
                    try:
                        kod = int(input(
                            "1.Добавление факультета\n2.Изменение факультета\n3.Просмотр факультетов\n4.Добавление студентов\n5.Измение данных студентов\n6.Просмотр успеваемости\n0.Выход: "))
                        match kod:
                            case 1:
                                faculties = input_faculty_data()
                            case 2:
                                name = input("Введите название факультета который вы хотите изменить: ")
                                t = False
                                for faculty in faculties:
                                    if name == faculty.get_name():
                                        change_faculty_data(faculty)
                                        t = True
                                if not t:
                                    print("Факультет с таким названием не найден")
                            case 3:
                                if len(faculties) != 0:
                                    print("\nФакультеты:")
                                    print_faculties(faculties)
                                else:
                                    print("Данных о факультетах нет")

                            case 4:
                                students = input_student_data()
                            case 5:
                                full_name = input("Введите Ф.И.О. студента данные которого вы хотите изменить: ")
                                t = False
                                for student in students:
                                    if full_name == student.get_full_name():
                                        change_student_data(student)
                                        t = True
                                if not t:
                                    print("Студент с таким Ф.И.О. не найден")
                            case 6:
                                if len(students) != 0:
                                    print("\nИнформация об успеваемости студентов:")
                                    print_student_performance(students)
                                else:
                                    print("Данных о студентах нет")
                            case 0:
                                break
                    except ValueError:
                        print("Необходимо ввести натуральное число")

            case 0:
                break
    except ValueError:
        print("Необходимо ввести натуральное число")
