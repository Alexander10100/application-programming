def create_alphabet():
    alphabet_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_high = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return alphabet_low, alphabet_high


def encryption(data, move, alphabet_low, alphabet_high):
    result = ''
    for i in data:
        if i not in alphabet_low and i not in alphabet_high:
            result += i
        else:
            count = alphabet_low.find(i.lower()) + move
            while count < 0 or count > len(alphabet_low) - 1:
                if count > len(alphabet_low) - 1:
                    count -= len(alphabet_low)
                elif count < 0:
                    count += len(alphabet_low)
            else:
                if i in alphabet_low:
                    result += alphabet_low[count]
                else:
                    result += alphabet_high[count]
    key = move * -1
    return result, key


def main():
    alphabet_low, alphabet_high = create_alphabet()
    print(f'Изменяемые символы - {alphabet_low} / {alphabet_high}')
    string = str(input('Введите строку, которую хотите зашифровать или расшифровать - '))
    step = input('Введите числом шаг сдвига для шифровки или расшифровки - ')

    try:
        int(step)
    except ValueError:
        print('Неверно введён шаг сдвига')
        return

    key, result = int(step), string

    if key / len(alphabet_low) == -1 or key / len(alphabet_low) == 1:
        print('Предупреждение. Результат ничем не будет отличатся')

    flag = 0
    while flag == 0:
        print('0 - шифровка/расшифровка\n'
              '1 - выход')
        operation = int(input('Введите номер нужной операций - '))
        if operation == 0:
            result, key = encryption(result, key, alphabet_low, alphabet_high)
            print(f'Результат - {result}')
            print('-------------------------------------------------')
        elif operation == 1:
            flag = 1
        else:
            print('Ошибка! Ведена несуществующая операция')


main()