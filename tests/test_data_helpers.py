import pytest
from ..app.helpers.data_dealers import str_to_list_of_int


class TestDataDeal:

    def test_str_to_int_list(self):
        assert str_to_list_of_int('1 2 3 4 ') == [1, 2, 3, 4]
