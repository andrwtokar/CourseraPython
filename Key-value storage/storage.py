import argparse
import os
import tempfile
import json

'''
Надо написать:
    1. функцию чтения из data-file слоавря                                  +
    2. функцию записи готового словаря в data-file                          +
    3. функцию чтения value по заданному key                                +
    4. функцию дозаписи заданного value в заданный key                      +
    5. реализовать механизм выбора действий                                 +
    6. разобраться в argparse и переделать программу под этот стиль         +
    7. -//- json -//-                                                       +
    8. сделать работу с файлом через tempfile                               +
'''

parser = argparse.ArgumentParser()
parser.add_argument('--key', dest="key", type=str)
parser.add_argument('--val', dest="value", type=str)
args = parser.parse_args()
"""
В переменной args мы имеем считанные значения:
    Значение    default
    key         None
    value       None
"""


def read_File(filename):
    """
    Аккуратно считываем данные из файла и записываем в словарь
    Открываем файл на дозапись для создания его, если он создан ещё не был
    :param filename: файл, из которого читаем данные
    :return: словарь с данными из файла
    """
    f = open(filename, 'a')
    f.close()
    with open(filename) as file:
        fileInternals = file.read()
        if fileInternals != "":
            result = json.loads(fileInternals)
        else:
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


def put_Dict_In_File(filename, dict):
    """
    Записывает рабочий словарь в файл filename
    :param filename: имя файля, в которых необходимо за писать словарь
    :param dict: словарь, который необходимо записать в файл
    :return: NONE
    """
    with open(filename, 'w') as f:
        json.dump(dict, f)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = read_File(storage_path)


if (args.value is None):
    result = read_Key(args.key, data)
    if not result is None:
        print(', '.join(result))
    else:
        print(result)
else:
    put_Key_Value(args.key, args.value, data)

put_Dict_In_File(storage_path, data)
