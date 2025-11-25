import sys
import pytest

sys.path.insert(0, 'src')

from sunbears.dataframe import DataFrame

def test_single_insert():
    df = DataFrame(["A", "B", "C"], [int, int, int], [])
    df.insert((1, 2, 3))
    assert df.rows == [(1, 2, 3)]

def test_multiple_insert():
    df = DataFrame(["A"], [int], [])
    for i in range(0, 1000):
        df.insert((i,))
        assert df.rows[i][0] == i
    assert len(df.rows) == 1000

def test_negative_integer():
    df = DataFrame(["A", "B"], [int, int], [])
    df.insert((-1, 0))
    assert df.rows[0] == (-1, 0)

def test_multiple_types():
    df = DataFrame(["A", "B", "C"], [int, float, str], [])
    df.insert((1, 2.5, "hello"))
    assert df.rows[0] == (1, 2.5, "hello")

def test_special_characters():
    df = DataFrame(["A"], [str], [])
    df.insert(["!@#$%^&*()"])
    assert df.rows[0][0] == "!@#$%^&*()"

def test_value_error():
    with pytest.raises(ValueError):
        df = DataFrame(["A", "B"], [int, int], [])
        df.insert((1, 2))
        df.insert((1, 2, 3))
        df.insert((1, ))
    
def test_type_error():
    with pytest.raises(TypeError):
        df = DataFrame(["A", "B", "C"], [int, int, int], [])
        df.insert((1, 2, 3))
        df.insert((4, 5, "six"))
