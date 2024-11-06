from parser import Parser
from dataframe import DataFrame, Filter, FilterOp, ValueType

p = Parser()
df = p.read_csv("data.csv")

projected_df = df.project(["id", "name"])

filtered_df = df.filter([Filter("salary", ValueType.IDENTIFIER, 10000.0, ValueType.CONSTANT, FilterOp.GREATER_THAN)])

count_df = df.project("salary").count()
sum_df = df.project("salary").sum()
average_df = df.project("salary").average()
max_df = df.project("salary").max()
min_df = df.project("salary").min()

new_df = df.filter([Filter("salary", ValueType.IDENTIFIER, 10000.0, ValueType.CONSTANT, FilterOp.GREATER_THAN)]).project(["id", "name"])
