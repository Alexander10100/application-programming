def entering_values(string, limitation):  # Ввод значении программы
    number = ckeck(string)
    if number < 1 or number > limitation:
        print('Введены некорректные данные. Попробуйте снова')
        return entering_values(string, limitation)
    else:
        return number


def creating_matrix(criteria):  # Создание и заполнение матрицы
    matrix = [[0] * criteria for i in range(criteria)]  # Создание 0 матрицы
    for i in range(criteria):
        for j in range(criteria):
            if i > j:
                matrix[i][j] = 1 / matrix[j][i]
            elif i == j:
                matrix[i][j] = 1
            elif j > i:
                matrix[i][j] = entering_values(f'Отношенее критерия {i+1} к {j+1} от 1 до 9: ', 9)
    return matrix


def calculation_coefficients(amount, amount_line):  # Расчёт коэффициентов
    coef = list(map(lambda x: round(x / amount, 2), amount_line))
    if sum(coef) != 1:
        difference = 1 - sum(coef)
        coef[0] += difference
    coef = list(map(lambda x: format(x, '.2f'), coef))
    return coef


def ckeck(string):  # Проверка на целое число
    n = input(string)
    try:
        n = int(n)
    except Exception:
        return 0
    return n


criteria = entering_values('Введите цифрой количество критериев: ', 1000)
matrix = creating_matrix(criteria)  # Создаем матрицу
amount_line = [sum(i) for i in matrix]  # Считаем сумму строк
amount = sum(amount_line)  # Подсчитываем общую сумму
coefficients = calculation_coefficients(amount, amount_line)  # Получаем коэффициенты
print(f'Весовые коэффициенты: {coefficients}')