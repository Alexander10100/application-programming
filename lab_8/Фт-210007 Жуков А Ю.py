import random
import logging


def out_keg(list_num, result):
    x = random.choice(list_num)
    print('Достали бочонок под номером ', x)
    list_num.remove(x)
    result.append(x)
    return list_num, result


N = int(input('Введите числом количество бочонков - '))
result = []
numbers = [i for i in range(1, N+1)]
print(numbers)

flag = 0
while flag != 3:
    print('1 - вытаскиваем один боченок\n'
          '2 - вытаскиваем боченки пока они не закончатся\n'
          '3 - прервать операции')
    flag = int(input('Укажите номер нужной операции - '))
    if flag == 1:
        numbers, result = out_keg(numbers, result)
    elif flag == 2:
        for i in range(len(numbers)):
            numbers, result = out_keg(numbers, result)
    print(result)
    print(numbers)
print(result)

