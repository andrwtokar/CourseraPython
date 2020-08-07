import sys
import argparse

'''
Надо написать:
    1. функцию чтения из data-file слоавря                                  -
    2. функцию записи готового словаря в data-file                          -
    3. функцию чтения value по заданному key                                +
    4. функцию дозаписи заданного value в заданный key                      +
    5. реализовать механизм выбора действий                                 +
    6. разобраться в argparse и переделать программу под этот стиль         +
    7. -//- json -//-                                                       -
    8. сделать работу с файлом через tempfile                               -
'''

parser = argparse.ArgumentParser()
parser.add_argument('--key', dest="key", type=str)
parser.add_argument('--value', dest="value", type=str)
args = parser.parse_args()
"""
В переменной args мы имеем значения:
    Значение    default
    key         None
    value       None
"""


def read_File(filename):
    """
    Аккуратно считываем данные из файла и записываем в словарь
    :param filename: файл, из которого читаем данные
    :return: словарь с данными из файла
    """
    result = dict()
    return result


def read_Key(key_name, dict):
    """
    Ищем в словаре необходимый нам ключ и возвращаем его значение
    :param key_name: key, по которому необходимо искать value
    :param dict: словарь, с которым надо работать
    :return: value по заданному ключу
    """
    return dict.get(key_name, None)


def put_Key_Value(key, value, dict):
    """
    Ищет необходимый ключ и дозаписывает в его мнжество заданное значение
    :param key: в данный ключ необходимо дописать значение
    :param value: данное значение необходимо дописать в исходный ключ
    :param dict: словарь, с которым надо работать
    :return: NONE
    """
    if dict.get(key, None) is None:
        dict[key] = []
    dict[key].append(value)

def put_Dict_In_File(filename):
    """
    Записывает рабочий словарь в файл filename
    :param filename: имя файля, в которых необходимо за писать словарь
    :return: NONE
    """

dict = read_File("files/storage.data")

if (args.value is None):
    print(read_Key(args.key, dict))
else:
    put_Key_Value(args.key, args.value, dict)

