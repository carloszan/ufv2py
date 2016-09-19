# -*- coding: utf-8 -*-


def str_to_list_of_int(elements):
    try:
        return [int(element) for element in elements.strip().split()]
    except:
        raise Exception('Only numbers')
