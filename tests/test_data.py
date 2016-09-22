# -*- coding: utf-8 -*-
import pytest
from ..app.models.data import Data


class TestData:

    def test_data__init(self):
        data = Data({'x': [1, 1], 'y': [1, 2], 'z': [1, 3]})
        assert data.x == [1, 1]
        assert data.y == [1, 2]
        assert data.z == [1, 3]

        data = Data({'x': [1, 1], 'y': [1, 2]})
        with pytest.raises(AttributeError):
            assert data.z == 1
