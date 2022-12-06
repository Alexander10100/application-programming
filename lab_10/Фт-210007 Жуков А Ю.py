def check(string):  # Проверка на целое число
    n = input(string)
    try:
        n = int(n)
    except Exception:
        print('Введено не натуральное числоо. Попробуйте снова')
        return check(string)
    return int(n)


def subtraction(banknotes, N, i):
    if N - banknotes[i][0] >= 0:
        N -= banknotes[i][0]
        banknotes[i][1] = banknotes[i][1] + 1
        return subtraction(banknotes, N, i)
    else:
        return N, banknotes


banknotes_denominations = [64, 32, 16, 8, 4, 2, 1]
quantity_banknotes = [0 for i in range(len(banknotes_denominations))]
N = check('Натуральное число ')
required_banknotes = list(zip(banknotes_denominations, quantity_banknotes))
required_banknotes = [list(k) for k in required_banknotes]
for i in range(len(required_banknotes)):
     N, required_banknotes = subtraction(required_banknotes, N, i)
print('Всего потребуется купюр ', sum([l[1] for l in required_banknotes]))
for j in required_banknotes:
    print(f'Купюр номиналом {j[0]} потребуется {j[1]}')