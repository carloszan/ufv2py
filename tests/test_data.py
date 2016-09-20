import pytest
from ..modules import str_to_list_of_int


class TestData:

    def test_str_to_int_list(self):
        assert str_to_list_of_int('1 2 3 4 ') == [1, 2, 3, 4]
