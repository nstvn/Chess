class Chess: #Создали класс для обработки координат
    def __init__(self):
        self.k = int(
            input('Введи координату первой клетки по горизонтали (1-8): '))  # x
        self.l = int(
            input('Введи координату первой клетки по вертикали (1-8): '))  # y
        self.m = int(
            input('Введи координату второй клетки по горизонтали (1-8): '))  # x2
        self.n = int(
            input('Введи координату второй клетки по вертикали (1-8): '))  # y2

    def check_color(self): #Создали функцию по сравнению цвета поля
        if (self.k + self.l + self.m + self.n) % 2 == 0:
            print('Поля одинакового цвета')
        else:
            print('Поля разного цвета')

    def ferz(self): #Создали функцию по проверке угрозы ферзя
        if (self.k == self.m) or (self.l == self.n) or (
                self.k - self.l == self.m - self.n) or (
                    self.k + self.l == self.m + self.n):
            print(f'Ферзь угрожает полю ({self.m}, {self.n})')
        else:
            print(f'Ферзь не угрожает полю ({self.m}, {self.n})')

    def koni(self): #Создали функцию по проверке угрозы коня
        if ((self.n - self.m == 2 or self.m - self.n == 2) and (self.k - self.l == 1 or self.k + self.l == 1)) or (
                (self.n - self.m == 1 or self.m - self.n == 1) and (self.l - self.k == 2 or self.k - self.l == 2)):
            print(f'Конь угрожает полю ({self.m}, {self.n})')
        else:
            print(f'Конь не угрожает полю ({self.m}, {self.n})')

    def ladia(self): #Создали функцию по проверке хода ладьи
        if self.k == self.m or self.l == self.n:
            print(f'Ладья дойдет за 1 ход на поле ({self.m}, {self.n})')
        else:
            print (f'Ладья дойдет за 2 хода. Поле первого хода ({self.m}, {self.l})')

    def progylka_ferzia(self): #Создали функцию по проверке хода ферзя
        if (self.k == self.m) or (self.l == self.n) or (
                self.k - self.l == self.m - self.n) or (
                    self.k + self.l == self.m + self.n):
            print(f'Ферзь дойдет за один ход на поле ({self.m}, {self.n})')
        else:
            print (f'Ферзь дойдет за 2 хода. Поле первого хода ({self.m}, {self.l})')

    def slon(self): #Создали функцию по проверке хода слона
        if (self.k - self.l == self.m - self.n) or (self.k + self.l == self.m + self.n):
            print(f'Слон дойдет за один ход на поле ({self.m}, {self.n})')
        elif (self.k + self.l + self.m + self.n) % 2 == 0:
            for x in range(1, 9):
                for y in range(1, 9):
                    if abs(x - self.k) == abs(y - self.l) and abs(x - self.m) == abs(y - self.n):
                        print(f'Слон дойдет за 2 хода. Поле первого хода ({x}, {y})')
        else:
            print('Слон не дойдет до второго поля')



a = Chess()
a.check_color()
a.ferz()
a.koni()
a.ladia()
a.progylka_ferzia()
a.slon()
