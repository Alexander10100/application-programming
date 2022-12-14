import logging


def beats_or_not(x2, y2, conditions):  # Бьёт фигура за один ход или нет
    flag = 1
    if conditions:
        print(f"Фигура бъет поле ({x2}; {y2}) за один ход")
    else:
        print(f"Не угрожает в данном ходе")
        flag = 0
    return flag


def elephant(x1, y1, x2, y2):  # Поиск координат для слона
    points = []
    for i in range(1, 9):
        for j in range(1, 9):
            if abs(x1 - i) == abs(y1 - j):
                points.append([i, j])
    for point in points:
        if abs(x2 - point[0]) == abs(y2 - point[1]):
            return point[0], point[1]


def colour(x1, y1, x2, y2):  # Определение цвета полей
    point1 = (x1 + y1) % 2
    point2 = (x2 + y2) % 2
    if point1 == point2:
        print("Заданные поля являются полями одного цвета")
    else:
        print("Поля разных цветов")
    return point1, point2


def entering_values(string, limitation):  # Ввод значении программы
    number = ckeck(string)
    if number < 1 or number > limitation:
        print('Введены некорректные данные. Попробуйте снова')
        logging.error('Incorrect number')
        return entering_values(string, limitation)
    else:
        return number


def ckeck(string):  # Проверка на целое число
    n = input(string)
    logging.info(f'Users input number {n}')
    try:
        n = int(n)
    except Exception:
        return 0
    return n


def menace(x1, y1, x2, y2, fig, point1, point2):  # Может ли фигура с поля (x1, y1) попасть на поле (x2, y2)
    modul_diffe_x = abs(x1 - x2)
    modul_diffe_y = abs(y1 - y2)
    if fig == 1:
        conditions = modul_diffe_x == 2 and modul_diffe_y == 1 or modul_diffe_x == 1 and modul_diffe_y == 2
        beats_or_not(x2, y2, conditions)
    elif fig == 2:
        conditions = modul_diffe_x == modul_diffe_y
        beats_2 = beats_or_not(x2, y2, conditions)
        if beats_2 == 0 and point1 == point2:
            x3, y3 = elephant(x1, y1, x2, y2)
            print(f"Для нападения переставьте фигуру на поле ({x3};{y3})")
        elif point1 != point2:
            print("Угроза невозможна")
    elif fig == 3:
        conditions = x1 == x2 or y1 == y2
        beats_2 = beats_or_not(x2, y2, conditions)
        if beats_2 == 0:
            print(f"Для нападения переставьте фигуру на поле ({x1};{y2})")
    elif fig == 4:
        conditions = modul_diffe_x == modul_diffe_y or x1 == x2 or y1 == y2
        beats_2 = beats_or_not(x2, y2, conditions)
        if beats_2 == 0:
            print(f"Для нападения передвиньте ферзя на поле ({x1};{y2})")
    else:
        print('Такой финуры нет')
        logging.error('Incorrect number')


logging.basicConfig(filename="logs.log", level=logging.INFO)
logging.info("User started program")
print('Координаты могут принимать значения от 1 до 8')
x1 = entering_values("Введите x координату первого поля - ", 8)
logging.info(f'x1 = {x1}')
y1 = entering_values("Введите y координату первого поля - ", 8)
logging.info(f'y1 = {y1}')
x2 = entering_values("Введите x координату второго поля - ", 8)
logging.info(f'x2 = {x2}')
y2 = entering_values("Введите y координату второго поля - ", 8)
logging.info(f'y2 = {y2}')

print("Выберите фигуру: 1 - Конь, 2 - Слон, 3 - Ладья, 4 - Ферзь")
fig = entering_values("Ваша фигруа - ", 4)
logging.info(f'figure = {fig}')

point1, point2 = colour(x1, y1, x2, y2)
menace(x1, y1, x2, y2, fig, point1, point2)
logging.info("Programm ended")