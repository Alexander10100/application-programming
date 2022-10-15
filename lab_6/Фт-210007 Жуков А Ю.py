def entering_values(string):
    number = ckeck(string)
    if number < 1 or number > 9:
        print('Введены некорректные данные. Попробуйте снова')
        return entering_values(string)
    else:
        return number


def creating_matrix(criteria):
    matrix = [[0] * criteria for i in range(criteria)]
    for i in range(criteria):
        for j in range(criteria):
            if i > j:
                matrix[i][j] = 1 / matrix[j][i]
            elif i == j:
                matrix[i][j] = 1
            elif j > i:
                matrix[i][j] = entering_values(f'Отношенее критерия {i+1} к {j+1} ')
    return matrix


def calculation_coefficients(amount, amount_line):
    coef = list(map(lambda x: round(x / amount, 2), amount_line))
    if sum(coef) != 1:
        difference = 1 - sum(coef)
        coef[0] += difference
    coef = list(map(lambda x: format(x, '.2f'), coef))
    return coef


def ckeck(string):
    n = input(string)
    try:
        n = int(n)
    except Exception:
        return 0
    return n


criteria = entering_values('Введите цифрой количество критериев: ')
matrix = creating_matrix(criteria)
amount_line = [sum(i) for i in matrix]
amount = sum(amount_line)
coefficients = calculation_coefficients(amount, amount_line)
print(f'весовые коэффициенты: {coefficients}')