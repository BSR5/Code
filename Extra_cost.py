import pandas as pd


def column_data(file_name, column_name):
    data = pd.read_csv(file_name)
    column = data[column_name]
    return column

def sort_data_in_column(column1, column2):
    zipped_column = list(zip(column1))
    sorted_column = sorted(zipped_column, reverse = True)
    column2_counted = len(column2)
    top_num_column = sorted_column[:column2_counted]
    return [value for value, *_ in top_num_column]

def sum_of_column(column, column2):
    column = [float(x) for x in column]
    column2 = [float(x) for x in column2]
    sum_column1 = sum(column)
    sum_column2 = sum(column2)
    result =  sum_column1 - sum_column2
    return result
