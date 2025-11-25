import sys
import pytest

sys.path.insert(0, 'src')

from sunbears.dataframe import DataFrame

def test_remove_one_row():
    df = DataFrame(["A", "B", "C"], [int, float, str], [(1, 1.5, "A"), (2, 1.5, "B"), (3, 2.5, "C"), (4, 1.0, "B"), (5, -1.0, "A")])
    df.remove(0)
    assert str(df).strip() == """+---+------+---+
| A | B    | C |
+---+------+---+
| 2 | 1.5  | B |
| 3 | 2.5  | C |
| 4 | 1.0  | B |
| 5 | -1.0 | A |
+---+------+---+""".strip()

def test_remove_multiple_rows():
    df = DataFrame(["A", "B", "C"], [int, float, str], [(1, 1.5, "A"), (2, 1.5, "B"), (3, 2.5, "C"), (4, 1.0, "B"), (5, -1.0, "A")])
    df.remove(0)
    df.remove(2)
    df.remove(4)
    assert str(df).strip() == """+---+-----+---+
| A | B   | C |
+---+-----+---+
| 2 | 1.5 | B |
| 4 | 1.0 | B |
+---+-----+---+""".strip()

def test_remove_out_of_bound():
    with pytest.raises(IndexError): 
        df = DataFrame(["A", "B", "C"], [int, float, str], [(1, 1.5, "A"), (2, 1.5, "B"), (3, 2.5, "C"), (4, 1.0, "B"), (5, -1.0, "A")])
        df.remove(5)
