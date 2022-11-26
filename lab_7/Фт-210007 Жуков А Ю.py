def beats_or_not(x2, y2, conditions):
    flag = 1
    if conditions:
        print(f"Фигура бъет поле ({x2}; {y2}) за один ход")
    else:
        print(f"Не угрожает в данном ходе")
        flag = 0
    return flag


def elephant(x1, y1, x2, y2):
    points = []
    for i in range(1, 9):
        for j in range(1, 9):
            print(i,' ', j)
            if abs(x1 - i) == abs(y1 - j):
                points.append([i, j])
    print(points)
    for point in points:
        if abs(x2 - point[0]) == abs(y2 - point[1]):
            return point[0], point[1]


print('Координаты могут принимать значения от 1 до 8')
x1 = int(input("Введите x координату первого поля - "))
y1 = int(input("Введите y координату первого поля - "))
x2 = int(input("Введите x координату второго поля - "))
y2 = int(input("Введите y координату второго поля - "))

print("Выберите фигуру: 1 - Конь, 2 - Слон, 3 - Ладья, 4 - Ферзь")
fig = int(input("Ваша фигруа - "))

point1 = (x1 + y1) % 2
point2 = (x2 + y2) % 2
if point1 == point2:
    print("Заданные координаты являются полями одного цвета")
else:
    print("Поля разных цветов")

modul_diffe_x = abs(x1-x2)
modul_diffe_y = abs(y1-y2)
if fig == 1:
    conditions = modul_diffe_x == 2 and modul_diffe_y == 1 or modul_diffe_x == 1 and modul_diffe_y == 2
    beats_2 = beats_or_not(x2, y2, conditions)
elif fig == 2:
    conditions = modul_diffe_x == modul_diffe_y
    beats_2 = beats_or_not(x2, y2, conditions)
    if beats_2 == 0 and point1 == point2:
        x3, y3 = elephant(x1, y1, x2, y2)
        print(f"Для нападения переставьте фигуру на поле ({x3};{y3})")
    elif point1 != point2:
        print('Угроза невозможна')
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