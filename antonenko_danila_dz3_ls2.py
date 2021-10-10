# С базовой логикой разобрался более сложное задание не понял, буду еще с функциями вникать


def thesaurus(*args):
    namelist = list(map(str, args))
    dict_names = {}
    for name in namelist:
        first_letter = name[0]
        dict_names[first_letter] = dict_names.get(first_letter, []) + [name]
    return dict_names


print(thesaurus('Артём', 'Антон', 'Илья', 'Иван', 'Максим', 'Мария', 'Данил', 'Денис'))

