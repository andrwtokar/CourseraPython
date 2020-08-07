import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key', dest="key", type=int)
parser.add_argument('--value', dest="value")

args = parser.parse_args();
print(args)

a = dict(s= [1, 2, 3, 4])
print(a)

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

put_Key_Value('d', 5, a)
put_Key_Value('s', 123, a)
put_Key_Value('Andrew', 20, a)

print(a)

def read_Key(key_name, dict):
    """
    Ищем в словаре необходимый нам ключ и возвращаем его значение
    :param key_name: key, по которому необходимо искать value
    :param dict: словарь, с которым надо работать
    :return: value по заданному ключу
    """
    return dict.get(key_name, None)

print(read_Key('s', a), '\n',
      read_Key('d', a), '\n',
      read_Key("Natalia", a))