from random import randint
import logging


def more_less(guessed_number, number):
    if guessed_number > number:
        print('Загаданное число больше')
    elif guessed_number < number:
        print('Загаданное число меньше')


def guessing(guessed_number, attempts):
    for i in range(1, attempts + 1):
        print('Попытка №', i)
        number = ckeck('Введите число, которое, на ваш взгляд, загадал компьютер - ')
        if guessed_number == number:
            print('Вы отгадали!!! С попытки №', i)
            return
        elif guessed_number != number:
            print('Неправильно. Осталось попыток:', attempts - i)
            if attempts - i != 0:
                more_less(guessed_number, number)
        if i == 6:
            print('Сегодня не ваш день.')
        print('')
    print('Вы не смогли отгадать число. Загаданное число -', guessed_number)


def ckeck(string):
    n = input(string)
    logging.info(f'Users input number {n}')
    try:
        n = int(n)
    except Exception:
        print('Введено не целое число. Попробуйте снова')
        logging.error('Incorrect number')
        return ckeck(string)
    return int(n)


print('Компьютер загадывает целое число от 1 до N. Ваша цель угадать его.')
N = ckeck('Введите N - ')
attempts = ckeck('Введите числом количество попыток - ')
guessed_number = randint(1, N)
guessing(guessed_number, attempts)
