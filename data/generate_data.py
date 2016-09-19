# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:08:31 2016

@author: carlos
"""

import pickle as pkl


def generate(data, file_path):
    """
    dump data that is passed by an argument
    """
    try:
        pkl.dump(data, open(file_path, 'wb'))
    except:
        raise Exception("Erro ao gerar arquivo")


def open(file_path):
    """
    return data whose was dumped by generate_data
    """
    try:
        return pkl.load(open(file_path, 'rb'))
    except:
        raise Exception("Erro ao ler arquivo")
