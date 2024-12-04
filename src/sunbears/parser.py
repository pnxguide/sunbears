from sunbears.dataframe import DataFrame

def infer_type(val):
    try:
        int(val)
        return int
    except ValueError:
        try:
            float(val)
            return float
        except ValueError:
            return str

class Parser:
    def read_csv(self, filepath: str) -> DataFrame:
        f = open(filepath, "r")
        content = f.readlines()

        # Get the column names as a list of str
        header_line = content[0].strip()
        column_names = header_line.split(",")

        # Infer each column type and append data into rows
        i = 1
        n = len(content)
        column_types = [int, int, int]
        rows = []
        for i in range(1, n):
            stripped_line = content[i].strip()
            tokens = stripped_line.split(",")

            tuple_list = []

            for j in range(len(tokens)):
                inferred_type = infer_type(tokens[j])
                inferred_token = inferred_type(tokens[j])
                
                if inferred_type == str:
                    column_types[j] = str
                elif inferred_type == float and column_types[j] != str:
                    column_types[j] = float

                tuple_list.append(inferred_token)
            
            rows.append(tuple(tuple_list))
            i = i + 1

        return DataFrame(column_names, column_types, rows)
