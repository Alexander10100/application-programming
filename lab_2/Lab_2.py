units = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
units_thousand = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
tens_10_19 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
              "семнадцать", "восемнадцать", "девятнадцать"]
tens = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]


def number_interpretation(remains_division, result_string, number, intermediate_string):  # Перевод самих цифр
    part_string, number_pass = '', ''
    if number == 0:
        part_string = ''
    elif remains_division == 1:
        if len(intermediate_string) > 3:
            if number == int(intermediate_string[-4]):
                part_string = units_thousand[number - 1]
        else:
            part_string = units[number - 1]
    elif remains_division == 2:
        if 2 > number > 0:
            number_pass = intermediate_string[1:2]
            part_string = tens_10_19[int(number_pass)]
            intermediate_string = intermediate_string[1:]
        else:
            part_string = tens[number - 2]
    elif remains_division == 0:
        part_string = hundreds[number - 1]
    result_string += part_string + ' '
    return result_string, intermediate_string, number_pass


def thousand(original_string):  # Правильность написание тысячи
    x = int(original_string[-5:-3])
    if x == 1:
        return 'тысяча '
    elif x == 2:
        return 'тысячи '
    elif 2 < x < 20 or x == 0:
        return 'тысяч '
    elif 19 < x < 100:
        return thousand(original_string[-4:])


def rub(original_string):  # Правильность написание рубля
    x = int(original_string[-2:])
    if x == 1:
        return 'рубль'
    elif 1 < x < 5:
        return 'рубля'
    elif 4 < x < 20 or x == 0:
        return 'рублей'
    elif 19 < x < 100:
        return rub(original_string[-1:])


def translate(original_string):
    result_string, number_pass = '', ''
    intermediate_string = original_string
    for number in original_string:
        if number_pass == number:
            continue
        remains_division = len(intermediate_string) % 3
        result_string, intermediate_string, number_pass = number_interpretation(remains_division, result_string,
                                                                                int(number), intermediate_string)
        intermediate_string = intermediate_string[1:]
        if len(intermediate_string) == 3:
            result_string += thousand(original_string)
        if len(intermediate_string) == 0:
            result_string += rub(original_string)
    return result_string


original_string = str(input('Ведите число ')).replace(' ', '')
try:
    num = int(original_string)
except:
    print('Было введено не число')
else:
    string_processing = translate(original_string)
    string_processing = " ".join(string_processing.split()).capitalize()
    print(string_processing)
