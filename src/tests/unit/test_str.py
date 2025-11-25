import sys
import pytest

sys.path.insert(0, 'src')

from sunbears.dataframe import DataFrame

def test_empty_dataframe():
    df = DataFrame([], [], [])
    assert str(df).strip() == "Empty DataFrame"

def test_no_rows():
    df = DataFrame(["A", "B", "C"], [int, int, int], [])
    assert str(df).strip() == """+---+---+---+
| A | B | C |
+---+---+---+
+---+---+---+""".strip()

def test_single_row():
    df = DataFrame(["A", "B", "C"], [int, int, int], [(1, 2, 3)])
    assert str(df).strip() == """+---+---+---+
| A | B | C |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+""".strip()

def test_multiple_rows():
    df = DataFrame(["A", "B", "C"], [int, int, int], [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    assert str(df).strip() == """+---+---+---+
| A | B | C |
+---+---+---+
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
+---+---+---+""".strip()

def test_single_row_multiple_sizes():
    df = DataFrame(["A", "B", "C"], [int, int, int], [(1, 23, 456)])
    assert str(df).strip() == """+---+----+-----+
| A | B  | C   |
+---+----+-----+
| 1 | 23 | 456 |
+---+----+-----+""".strip()

def test_multiple_rows_multiple_sizes():
    df = DataFrame(["A", "B", "C"], [int, int, int], [(1, 23, 456), (7890, 1, 23)])
    assert str(df).strip() == """+------+----+-----+
| A    | B  | C   |
+------+----+-----+
| 1    | 23 | 456 |
| 7890 | 1  | 23  |
+------+----+-----+""".strip()

def test_single_row_multiple_types():
    df = DataFrame(["A", "B", "C"], [int, float, str], [(1, 2.34, "56789")])
    assert str(df).strip() == """+---+------+-------+
| A | B    | C     |
+---+------+-------+
| 1 | 2.34 | 56789 |
+---+------+-------+""".strip()

def test_multiple_row_multiple_types():
    df = DataFrame(["A", "B", "C"], [int, float, str], [(1, 2.34, "56789"), (12345, 6.7, "eight-nine")])
    assert str(df).strip() == """+-------+------+------------+
| A     | B    | C          |
+-------+------+------------+
| 1     | 2.34 | 56789      |
| 12345 | 6.7  | eight-nine |
+-------+------+------------+""".strip()
