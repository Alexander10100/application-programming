def input_sorting(string, quantity):
    common_list = []
    print(string)
    for i in range(1, quantity + 1):
        x = [[int(input(f'№{i} ')), i]]
        common_list += x
    return common_list


quantity = int(input('Введите кколичество сотрудников '))

string_distance = 'Введите расстояние в километрах от работы до дома каждого сотрудника по очереди.'
distance = input_sorting(string_distance, quantity)
distance.sort()

string_price = 'Введите тарифы в рублях за проезд одного километра в каждом такси по очереди.'
price = input_sorting(string_price, quantity)
price.sort(reverse=True)

#  Объединяем отсортированные значения
all_data = []
for j in range(quantity):
    all_data += [distance[j] + price[j]]

#  Выбираем номер такси для каждого сотрудника
result = sorted(all_data, key=lambda x: x[1])
number_taxi = []
for number in result:
    number_taxi.append(number[3])
print(number_taxi)


