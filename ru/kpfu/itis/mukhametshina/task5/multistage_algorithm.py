import csv
import operator
from itertools import combinations


def multistage_algorithm(all_items, dictionary):
    k = len(all_items)

    dict_with_one_item = {}
    dict_with_two_item = {}

    # singletons
    for bucket in dictionary:
        for item in dictionary[bucket]:
            if item in dict_with_one_item.keys():
                dict_with_one_item[item] = dict_with_one_item[item] + 1
            else:
                dict_with_one_item[item] = 1

    # Удаление
    for i in list(dict_with_one_item):
        if dict_with_one_item[i] / k < 0.015:
            all_items.pop(i, 3001)
            dict_with_one_item.pop(i, 3000)

    # doubletons
    combs = list(combinations(all_items.keys(), 2))
    # {0: {(item1, item2): 4}}
    for comb in combs:
        for bucket in dictionary:
            f = comb[0], comb[1] in dictionary[bucket]
            if comb[0] in dictionary[bucket] and comb[1] in dictionary[bucket]:
                hash_ = (all_items.get(comb[0]) + all_items.get(comb[1])) % k
                if hash_ in dict_with_two_item.keys():
                    if comb in dict_with_two_item[hash_].keys():
                        dict_with_two_item[hash_][comb] = dict_with_two_item[hash_][comb] + 1
                    else:
                        dict_with_two_item[hash_][comb] = 1
                else:
                    dict_with_two_item[hash_] = {comb: 1}

    list_on_dict = []
    for hash_ in dict_with_two_item:
        for comb in dict_with_two_item[hash_]:
            list_on_dict.append([hash_, comb, dict_with_two_item[hash_][comb]])
    list_on_dict.sort(key=lambda x: x[2])

    k = len(list_on_dict)

    # Запись в cvs
    with open("doubletons.csv", mode="w") as w_file:
        writer = csv.writer(w_file)
        writer.writerow(["HASH", "PRODUCTS", "COUNT"])
        for i in list_on_dict:
            if i[2] / k > 0.015:
                writer.writerow(i)

    sorted_x = sorted(dict_with_one_item.items(), key=operator.itemgetter(1))
    with open("singletons.csv", mode="w") as w_file:
        writer = csv.writer(w_file)
        writer.writerow(["PRODUCT", "COUNT"])
        for i in sorted_x:
            if i[1] / k > 0.15:
                writer.writerow(i)

    print(dict_with_one_item)
    print(dict_with_two_item)
    return dict_with_one_item, dict_with_two_item
