import sys

'''
Надо написать:
    1. функцию чтения из data-file слоавря
    2. функцию записи готового словаря в data-file
    3. функцию чтения value по заданному key
    4. функцию дозаписи заданного value в заданный key
    5. реализовать механизм выбора действий
    6. разобраться в argparse и переделать программу под этот стиль
    7. -//- json -//-
    8. сделать работу с файлом через tempfile
'''

input_command = sys.argv[1:len(sys.argv)]
"""
В массиве n мы имеем все введенные данные через консоль
"""


def read_File(filename):
    """
    Аккуратно считываем данные из файла и записываем в словарь
    :param filename: файл, из которого читаем данные
    :return: словарь с данными из файла
    """
    result = dict()
    return result


def read_Key(key_name):
    """
    Ищем в словаре необходимый нам ключ и записываем в value его значение
    :param key_name: key, по которому необходимо искать value
    :return: value по заданному ключу
    """
    value = 1;
    return value


def put_Key_Value(key, value):
    """
    ищет необходимый ключ и дозаписывает в его мнжество заданное значение
    :param key: в данный ключ необходимо дописать значение
    :param value: данное значение необходимо дописать в исходный ключ
    :return: NONE
    """


if len(input_command) == 2:
    value = read_Key(input_command[2])
    print(input_command + value)
elif len(input_command) == 4:
    put_Key_Value(input_command[2], input_command[4])
