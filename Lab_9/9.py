from random import randint
import logging


def more_less(guessed_number, number):
    if guessed_number > number:
        print('Загаданное число больше')
        logging.info(f'Program printed Загаданное число больше')
    elif guessed_number < number:
        print('Загаданное число меньше')


def guessing(guessed_number, attempts):
    for i in range(1, attempts + 1):
        print('Попытка №', i)
        logging.info(f'Попытка № {i}')
        logging.info(f'Program printed Введите число, которое, на ваш взгляд, загадал компьютер')
        number = ckeck('Введите число, которое, на ваш взгляд, загадал компьютер - ')
        if guessed_number == number:
            print('Вы отгадали!!! С попытки №', i)
            logging.info(f'Program printed Вы отгадали!!! С попытки № {i}')
            return
        elif guessed_number != number:
            print('Неправильно. Осталось попыток:', attempts - i)
            logging.info(f'Неправильно. Осталось попыток: {attempts - i}')
            if attempts - i != 0:
                more_less(guessed_number, number)
        if i == 6:
            print('Сегодня не ваш день.')
            logging.info(f'Program printed Сегодня не ваш день')
        print('')
    print('Вы не смогли отгадать число. Загаданное число -', guessed_number)
    logging.info(f'Program printed Вы не смогли отгадать число. Загаданное число - {guessed_number}')


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


logging.basicConfig(level=logging.DEBUG, filename="log.log", format="%(asctime)s %(levelname)s %(message)s")
logging.info('Programm started')
print('Компьютер загадывает целое число от 1 до N. Ваша цель угадать его.')
logging.info(f'Program printed Компьютер загадывает целое число от 1 до N. Ваша цель угадать его.')
logging.info(f'Program printed Введите N')
N = ckeck('Введите N - ')
logging.info(f'N = {N}')
logging.info(f'Program printed Введите числом количество попыток')
attempts = ckeck('Введите числом количество попыток - ')
logging.info(f'attempts = {attempts}')
guessed_number = randint(1, N)
logging.info(f'guessed_number = {guessed_number}')
guessing(guessed_number, attempts)
logging.info('Programms end')