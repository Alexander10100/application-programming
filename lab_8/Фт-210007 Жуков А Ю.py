import random
import logging


def out_keg(list_num, result):
    x = random.choice(list_num)
    print('Достали бочонок под номером ', x)
    list_num.remove(x)
    result.append(x)
    return list_num, result


def decision(numbers):
    result = []
    flag = 0
    while flag != 3:
        if len(numbers) == 0:
             return result
        print('1 - вытаскиваем один боченок\n'
              '2 - вытаскиваем боченки пока они не закончатся\n'
              '3 - прервать операции')
        flag = ckeck('Укажите номер нужной операции - ')
        if flag == 1:
            numbers, result = out_keg(numbers, result)
        elif flag == 2:
            for i in range(len(numbers)):
                numbers, result = out_keg(numbers, result)
        else:
            print('Такой операции нет!')


def ckeck(string):
    n = input(string)
    try:
        n = int(n)
    except Exception:
        print('Введено не целое число. Попробуйте снова')
        return ckeck(string)
    return int(n)


N = ckeck('Введите числом количество бочонков - ')
numbers = [i for i in range(1, N+1)]
result = decision(numbers)
print(f' Весь порядок {result}')