from enum import Enum
from typing import Self

class ValueType(Enum):
    IDENTIFIER = 1
    CONSTANT = 2

class FilterOp(Enum):
    EQUAL = 1
    NOT_EQUAL = 2
    LESS_THAN = 3
    LESS_THAN_OR_EQUAL = 4
    GREATER_THAN = 5
    GREATER_THAN_OR_EQUAL = 6

    def __str__(self):
        op_str = ["", "=", "!=", "<", "<=", ">", ">="]
        return f"{op_str[self.value]}"

class Filter:
    def __init__(self, lvalue: object, ltype: ValueType, rvalue: object, rtype: ValueType, op: FilterOp):
        self.lvalue = lvalue
        self.ltype = ltype
        self.rvalue = rvalue
        self.rtype = rtype
        self.op = op

    def __str__(self):
        return f"{self.lvalue} {self.op} {self.rvalue}"

class DataFrame:
    def __init__(self, column_names: list[str], column_types: list[type], rows: list[object]):
        self.column_names = column_names
        self.column_types = column_types
        self.rows = rows

    # TODO:
    def project(self, projected_column: list[str]) -> Self:
        print("Projecting:", projected_column)
        return DataFrame([], [], [])

    # TODO:
    def filter(self, filters: list[Filter]) -> Self:
        print("Filtering using:", end="")
        for f in filters:
            print(f" ({f})")
        return DataFrame([], [], [])

    # TODO:
    def count(self) -> int:
        print("Counting all the non-empty rows")
        return 0

    # TODO:
    def sum(self):
        # NOTE: Ensure there is only a single column and the column is either int or float
        print("Sum all the values")
        return 0

    # TODO:
    def average(self) -> float:
        # NOTE: Ensure there is only a single column and the column is either int or float
        print("Find the average of all the values")
        return 0

    # TODO:
    def max(self):
        print("Find the maximum value among all the values")
        return 0

    # TODO:
    def min(self):
        print("Find the minimum value among all the values")
        return 0

    def __str__(self):
        dataframe_string = ""

        # Print column names
        for i in range(len(self.column_names)):
            dataframe_string += f"{self.column_names[i]}:{str(self.column_types[i])}"
            if i < len(self.column_names) - 1:
                dataframe_string += "|"
        dataframe_string += "\n"

        # Print data
        for row in self.rows:
            for i in range(len(row)):
                dataframe_string += f"{row[i]}"
                if i < len(row) - 1:
                    dataframe_string += "|"
            dataframe_string += "\n"
        
        return dataframe_string
