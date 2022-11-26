import random
import logging


def out_keg(list_num, result):  # Сообщаем о бочонке и заносим результат
    x = random.choice(list_num)
    print('Достали бочонок под номером ', x)
    logging.info(f'Достали бочонок под номером {x}')
    list_num.remove(x)
    result.append(x)
    return list_num, result


def decision(numbers):  # Достаем бочонок
    result = []
    flag = 0
    while flag != 3:
        if len(numbers) == 0:
             return result
        print('1 - вытаскиваем один боченок\n'
              '2 - вытаскиваем боченки пока они не закончатся\n'
              '3 - прервать операции')
        flag = check('Укажите номер нужной операции - ')
        logging.info(f'Operation = {flag}')
        if flag == 1:
            numbers, result = out_keg(numbers, result)
        elif flag == 2:
            for i in range(len(numbers)):
                numbers, result = out_keg(numbers, result)
        else:
            print('Такой операции нет!')
            logging.error('Incorrect operation')


def check(string):  # Проверка на целое число
    n = input(string)
    logging.info(f'Users input number {n}')
    try:
        n = int(n)
    except Exception:
        print('Введено не целое число. Попробуйте снова')
        logging.error('Incorrect number')
        return check(string)
    return int(n)


logging.basicConfig(level=logging.DEBUG, filename="log.log")  # Создаем лог файл
N = check('Введите числом количество бочонков - ')
logging.info(f'N = {N}')
numbers = [i for i in range(1, N+1)]
result = decision(numbers)
print(f' Весь порядок {result}')
logging.info(f'Sequence = {result}')