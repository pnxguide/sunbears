# Assignment #0 - Tiny Data Processing Library

![sunbears, not your pandas alternative](thumbnail.png)

You will be implementing a tiny data processing library that has capabilities similarly to `pandas` and `polars`. The name is , namely `sunbears`.

<center>
<b>This is a solo assignment; you cannot collaborate in any cases.<br>You can only share your high-level ideas (i.e., not a code) and Python basics.</b>
<br><br>
<b>START EARLY!<br>I believe that this is the hardest programming assignment you have encountered so far.</b>
</center>

## Prerequisite and Dependencies
If you do not have the following software installed, please install them before you begin.

- At least Python 3.12

## Getting Started
Clone the repository into your local workspace. Make sure that you have at least Python 3.12 installed on it. To clone, you may use the following CLI command.

```sh
git clone https://github.com/pnxguide/sunbears
```

If you do not have `git` installed on your workspace, you can use the download ZIP option on the github website.

**Please do not upload your cloned repository publicly.** This can be interpreted the same as plagiarism, since you are trying to let the others see your work.

## DataFrame
`sunbears`'s DataFrame is an abstract data type that represents a table. The DataFrame can have multiple columns with multiple data types. You should be able to support at least 3 data types: `int`, `float`, and `str`. The DataFrame can also have multiple rows of data that match the specification of the columns.

Users can create the DataFrame instance through its constructor function. The function requires users to provide:

- A list of column names (as a list of `str`)
- A list of column types (as a list of `type`)
  - You can extract the type of the variable by using class `type` (https://docs.python.org/3/library/functions.html#type)
- A list of rows (as a list of `tuple`)
  - You can learn more about `tuple` here (https://docs.python.org/3/library/stdtypes.html#tuple)

Moreover, users can assess the DataFrame through different DataFrame's methods:

- `project` is to create another DataFrame based on the current DataFrame instance. The new DataFrame can have different ordering of columns or some of the columns in the current DataFrame may be dropped in the new DataFrame.
- `filter` is to create another DataFrame based on the current DataFrame instance by removing some rows that do not meet the given conditions. To specify a condition, users need to use class `Filter`, which will allow users to create an instance of a condition.
  - Creating a `Filter` instance requires users to specify the condition in the `[l-value] [op] [r-value]` fashion:
    - `[l-value]` and `[r-value]` are values on each side. Each of them can be either `IDENTIFIER` (or a column name) or `CONSTANT`
    - `[op]` is the operator. There are 6 operators supported in the DataFrame:
      - `EQUAL`: `[l-value]` must be equal to `[r-value]`
      - `NOT_EQUAL`: `[l-value]` must not be equal to `[r-value]`
      - `LESS_THAN`: `[l-value]` must be less than `[r-value]`
      - `LESS_THAN_OR_EQUAL`: `[l-value]` must be less than or equal to `[r-value]`
      - `GREATER_THAN`: `[l-value]` must be greater than `[r-value]`
      - `GREATER_THAN_OR_EQUAL`: `[l-value]` must be greater than or equal to `[r-value]`
  - For example, if a user wants to specify `age <= 20`, the user needs to create the following Filter instance:
    - `Filter("age", ValueType.IDENTIFIER, FilterOp.LESS_THAN_OR_EQUAL, 20, ValueType.CONSTANT)`
- `count` is to count all the non-empty rows in the current DataFrame instance.
- `sum` is to sum all the values in a column of the current DataFrame instance. For simplicity, you need to check whether the DataFrame has only a single `int` or `float` column or not. If not, you must throw an error.
- `average` is to find an average of all the values in a column of the current DataFrame instance. For simplicity, you need to check whether the DataFrame has only a single `int` or `float` column or not. If not, you must throw an error.
- `max` is to find a maximum value among all the values in a column of the current DataFrame instance. For simplicity, you need to check whether the DataFrame has only a single `int` or `float` column or not. If not, you must throw an error.
- `min` is to find a minimum value among all the values in a column of the current DataFrame instance. For simplicity, you need to check whether the DataFrame has only a single `int` or `float` column or not. If not, you must throw an error.
- `__str__` is a function for converting the DataFrame instance into `str`. You need to format the instance as in the following format.

```
column1|column2|...|columnn
1|Nueng|...|3.5
2|Poom|...|2.5
3|Indy|...|1.5
```

## Parser
However, it is a bit difficult to import data from external sources into the DataFrame instance if users need to use the constructor manually. Therefore, `sunbears` provides a class, namely Parser, to accomodate this. The Parser is a class providing a capability to convert a CSV (comma-separated values) file into the DataFrame.

## Guideline for Implementing `sunbears`
For each step, you should try to run a test along the way. This will ensure that your implementation is correct.

1) You need to understand the specification of `sunbears`'s DataFrame and parser.
2) Implement the parser.
3) Implement the `__str__` method in the `DataFrame` class. You may want to use this to debug your further implementation.
4) Implement the `project` method in the `DataFrame` class.
5) Implement the `filter` method in the `DataFrame` class.
6) Implement the `count`, `sum`, and `average` methods in the `DataFrame` class.
  - To find an average, recall that average is actually `sum` divided by `count`. You may want to reuse `count` and `sum`.
7) Implement the `max` and `min` methods in the `DataFrame` class.
  - To compute `max` and `min`, you need to loop through all the elements.

## Verifying Your Implementation
You can use `src/test.py` to verify the correctness of your implementation. However, it is not complete and rigorous. You should add more tests to ensure that your implementation is completely correct.

**You need to think about edge cases and try running them.**

## Grading
There will be no grade for completing this programming assignment. However, you will not be able to receive any grade for the programming assignment unless you complete this.

On completion, you must have a fully-functional `sunbears` package along with a decent test suite. You also need to be **checked out** in order to redeem a certification of success. An inability to obtain this will lead to no points in the *Skill Set #3 - System Programming*.

## Need Help
**You must not collaborate with your friends.** If you offer your friend a help, you will also be marked as cheated.

I am not recommending you to use Generative AI (e.g., ChatGPT) if it does not make you understand. **Do not forget that you will be interviewed in the end.**

Since you cannot collaborate, I may conduct a quick Python tutorial session in the weekend. Please feel free to join. There will also be an online recording available shortly.