from typing import Self

class DataFrame:
    """
    DataFrame is a class that represents a table-like data structure
    in Python.
    """

    """
    TODO(P1): Describe your rational for the file format you will use to
        store a DataFrame object.
    """

    def __init__(
        self,
        column_names: list[str] = None,
        column_types: list[type] = None,
        rows: list[tuple] = None,
    ):
        """
        TODO(P1): 
        - Modify this constructor as needed
        - Write a docstring for this constructor
          (You should remove this TODO(P1): and replace with your docstring)
        """

        self.column_names = column_names
        self.column_types = column_types
        self.rows = rows

        if self.column_names == None:
            self.column_names = []
        if self.column_types == None:
            self.column_types = []
        if self.rows == None:
            self.rows = []

        # TODO(P1): Your code here


    def insert(self, row: tuple) -> None:
        """
        TODO(P1):
        - Implement this method as required in the specification
        - Write a docstring for this method
          (You should remove this TODO(P1): and replace with your docstring)
        """

        # TODO(P1): Your code here

    def remove(self, index: int) -> None:
        """
        TODO(P1):
        - Implement this method as required in the specification
        - Write a docstring for this method
          (You should remove this TODO(P1): and replace with your docstring)
        """

        # TODO(P1): Your code here

    def persist_to_disk(self, file_path: str) -> None:
        """
        TODO(P1):
        - Implement this method as required in the specification
        - Write a docstring for this method
          (You should remove this TODO(P1): and replace with your docstring)
        """

        # TODO(P1): Your code here

    def load_from_disk(self, file_path: str) -> Self:
        """
        TODO(P1):
        - Implement this method as required in the specification
        - Write a docstring for this method
          (You should remove this TODO(P1): and replace with your docstring)
        """

        # TODO(P1): Your code here

    def __str__(self):
        """
        TODO(P1):
        - Modify this method to not display removed rows
        - Write a docstring for this method
          (You should remove this TODO(P1): and replace with your docstring)
        """

        if len(self.column_names) == 0:
            return "Empty DataFrame"
        
        col_widths = []
        for i in range(len(self.column_names)):
            max_w = len(self.column_names[i])
            for row in self.rows:
                w = len(str(row[i]))
                if w > max_w:
                    max_w = w
            col_widths.append(max_w)

        lines = []
        
        separator = "+-" + "-+-".join(["-" * w for w in col_widths]) + "-+"
        
        lines.append(separator)
        
        # Header Row
        header_cells = [h.ljust(col_widths[i]) for i, h in enumerate(self.column_names)]
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append(separator)
        
        # Data Rows
        for row in self.rows:
            row_cells = [str(r).ljust(col_widths[i]) for i, r in enumerate(row)]
            lines.append("| " + " | ".join(row_cells) + " |")
            
        lines.append(separator)

        return "\n".join(lines)
