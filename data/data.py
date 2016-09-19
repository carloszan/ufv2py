# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:08:31 2016

@author: carlos
"""

import pickle as pkl
import numpy as np


def generate_data_b(data, file_path):
    """
    dump data that is passed by an argument
    """
    try:
        pkl.dump(data, open(file_path, 'wb'))
    except:
        raise Exception("Erro ao gerar arquivo")
 

def open_data_b(file_path):
    """
    return data whose was dumped by generate_data
    """
    try:
        return pkl.load(open(file_path, 'rb'))
    except:
        raise Exception("Erro ao ler arquivo")
      

"""
Ajustes:
1) Versão generalizada de open_data_t (para fins que não sejam de gráficos) V
2) Colocar o annotate
3) Ligar pontos com linhas V
4) Colocar rótulos nos pontos do scatter plot, contendo o número da iteração onde foi encontrado aquele valor V
"""

def open_data_t(file_path):
    """
    return a dictonary with x, y and z and time 
    """
    
    #first, we create a data which is a hash
    #then we create indices depending on how columns has the file
    #so, we put some empty np arrays because we will append it later
    #open the file, remove data we dont use like time, error and indices
    
    data = {}
    indices = []
    a = open(file_path, 'r')
    tam = len(a.readline().split()) - 3
    a.close()   
    for x in range(1,tam,1):
        indices.append("alfa"+str(x))
        
    for indice in indices:
                data[indice] = np.asarray([])
    data['time']  = np.asarray([])
    data['error'] = np.asarray([])
    data['i']     = np.asarray([])    
    
    with open(file_path, 'r') as f:
        interaction = 0
        for line in f:
            l = line.strip().split()
        
            time = float(l[-1])
            error = float(l[-2])
            
            #delete data we dont use
            l.pop(0)
            l.pop(-1)
            l.pop(-1)            
            
            #transform all strings to float using list comprehension
            l = [float(i) for i in l]
            
            #its important to walk n and indice together and transform
            #temp to a list
            for n, indice in zip(range(len(l)-1), indices):
                temp = l[0] + l[n+1]     
                data[indice] = np.append(data[indice], [temp])
            
            data['time']  = np.append(data['time'],  [time])
            data['error'] = np.append(data['error'], [error])            
            data['i']     = np.append(data['i'],     [interaction])          
            
            interaction += 1
    return data
    

def str_to_list_of_int(elements):
    try:
        return [int(element) for element in elements.strip().split()]
    except:
        raise Exception('Apenas numeros devem ser informados')    