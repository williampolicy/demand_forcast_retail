# 文件路径: tests/test_module1.py

import pytest
from kangforecast.module1 import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
