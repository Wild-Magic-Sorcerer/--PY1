def get_count_char(str_):
    dic = {}
    for char in str_:
        if not char.isalpha():
            continue
        else:
            charl = char.lower()
            if dic.get(charl) is None:
                dic[charl] = 1
            else:
                dic[charl] += 1
    return dic

def get_proc_char(dic_):
    for i in dic_:
        dic_[i] = str(round(dic_[i]/len(dic_), 5) * 100) + "%"
    return dic_


main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

print(get_proc_char(get_count_char(main_str)))
