# -*- coding: utf-8 -*-
import pytest
from ..app.helpers.data_dealers import *


class TestDataDealers:

    def test_str_to_int_list(self):
        assert str_to_list_of_int('1;2;3;4 ') == [1, 2, 3, 4]

    def test_raise_error_str_to_int_list(self):
        with pytest.raises(Exception):
            str_to_list_of_int('1;2 d')

    def test_open_csv_to_array(self):
        f = open('tests/t.csv', 'r')

        x = y = []
        x, y = csv_to_array(f)

        assert x == [1, 3, 5, 7]
        assert y == [2, 4, 5, 9]
