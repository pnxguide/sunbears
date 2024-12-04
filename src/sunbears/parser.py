from sunbears.dataframe import DataFrame

def interpret(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val

class Parser:
    # TODO:
    def read_csv(self, filepath: str) -> DataFrame:
        f = open(filepath, "r")
        content = f.readlines()
        print(content)

        # TODO: Get the column names as a list of str
        header_line = content[0].strip()
        column_names = header_line.split(",")

        # TODO: Infer each column type
        i = 1
        n = len(content)
        column_types = [int, int, int]
        while i < n:
            stripped_line = content[i].strip()
            tokens = stripped_line.split(",")

            for j in range(len(tokens)):
                inferred_token = interpret(tokens[j])
                inferred_type = type(inferred_token)

                if inferred_type == str:
                    column_types[j] = str
                elif inferred_type == float and column_types[j] != str:
                    column_types[j] = float

            i = i + 1

        print(column_types)

        # TODO: Get all the rows as a list of tuples

        return DataFrame(column_names, column_types, [])
