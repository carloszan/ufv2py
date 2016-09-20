# -*- coding: utf-8 -*-


class Data():

    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']

        if kwargs.get('z'):
            self.z = kwargs['z']
