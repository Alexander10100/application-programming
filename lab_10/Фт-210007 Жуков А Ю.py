def check(string):  # Проверка на целое число
    n = input(string)
    try:
        n = int(n)
    except Exception:
        return 0
    return n


def entering_values(string, limitation):  # Ввод значении программы
    number = check(string)
    if number < 1 or number > limitation:
        print('Введено не натуральное числоо или слишком большое. Попробуйте снова')
        return entering_values(string, limitation)
    else:
        return number


def subtraction(banknotes, N, i):  # вычитание определенного номинала банкноты из числа
    if N - banknotes[i][0] >= 0:
        N -= banknotes[i][0]
        banknotes[i][1] = banknotes[i][1] + 1
        return subtraction(banknotes, N, i)
    else:
        return N, banknotes


banknotes_denominations = [64, 32, 16, 8, 4, 2, 1]
quantity_banknotes = [0 for i in range(len(banknotes_denominations))]
N = entering_values('Натуральное число, не больше чем 60000 - ', 60000)  # ввод числа с ограничением из-за рекурсии
required_banknotes = list(zip(banknotes_denominations, quantity_banknotes))  # создание списка из кортежей
required_banknotes = [list(k) for k in required_banknotes]
for i in range(len(required_banknotes)):
    N, required_banknotes = subtraction(required_banknotes, N, i)
print('Всего потребуется купюр', sum([l[1] for l in required_banknotes]))
for j in required_banknotes:
    print(f'Купюр номиналом {j[0]} потребуется {j[1]}')