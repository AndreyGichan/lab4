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

            case 0:
                break
    except ValueError:
        print("Необходимо ввести натуральное число")
