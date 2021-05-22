import csv

from ru.kpfu.itis.mukhametshina.task5.multistage_algorithm import multistage_algorithm

dictionary = dict()
all_items = dict()
# {basket: [item1, item2]}
# Чтение и список всех продуктов и корзин
with open('transactions.csv') as File:
    reader = csv.reader(File, delimiter=';')
    count = 1
    for row in reader:
        if row[0] not in all_items.keys():
            all_items[row[0]] = count
            count = count + 1
        if row[1] in dictionary.keys():
            dictionary[row[1]].append(row[0])
        else:
            dictionary[row[1]] = []
            dictionary[row[1]].append(row[0])

# Возвращает singletons и doubletons и записывает их в csv файл
singletons, doubletons = multistage_algorithm(all_items, dictionary)