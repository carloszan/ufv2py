# -*- coding: utf-8 -*-


def str_to_list_of_int(elements):
    try:
        return [int(element) for element in elements.strip().split(';')]
    except:
        raise Exception('Only numbers')


def csv_to_array(file):
    _x = []
    _y = []
    elements = file.read().split()
    for element in elements:
        e = str_to_list_of_int(element)
        _x.append(e[0])
        _y.append(e[1])
    return _x, _y
