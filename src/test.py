from sunbears.parser import Parser
from sunbears.dataframe import DataFrame, Filter, FilterOp, ValueType

p = Parser()
df = p.read_csv("data.csv")
print(df)

projected_df = df.project(["id", "name"])
print(projected_df)

filtered_df = df.filter([Filter("salary", ValueType.IDENTIFIER, 10000.0, ValueType.CONSTANT, FilterOp.GREATER_THAN)])
print(filtered_df)

count_df = df.project("salary").count()
sum_df = df.project("salary").sum()
average_df = df.project("salary").average()
max_df = df.project("salary").max()
min_df = df.project("salary").min()
print(count_df, sum_df, average_df, max_df, min_df)

new_df = df.filter([Filter("salary", ValueType.IDENTIFIER, 10000.0, ValueType.CONSTANT, FilterOp.GREATER_THAN)]).project(["id", "name"])
print(new_df)
