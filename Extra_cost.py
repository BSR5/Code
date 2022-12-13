import pandas as pd

# Gathers data from the "charges" column in the later defined csv file
def column_data(file_name, column_name):
    data = pd.read_csv(file_name) # Reads the DataFrame into the "data" variable
    column = data[column_name]  # Gets the data from the "Charges" column and saves it to the "column variable"
    return column

# Sortes the data in a specified column into reverse order
def sort_data_in_column(column1, column2):
    zipped_column = list(zip(column1)) # Turns the tupled data into a single list
    sorted_column = sorted(zipped_column, reverse = True) # Sorts the column into reverse order
    column2_counted = len(column2) # Counts the length of how many items in column 2
    top_num_column = sorted_column[:column2_counted] #selects the top results matching column2
    return [value for value, *_ in top_num_column] # Extracts the values from the tuples in the "top_num_column1" list and returns it to the call

# Adds the defined columns together
def sum_of_column(column, column2):
    column = [float(x) for x in column] # Convert the strings in the column to numbers
    column2 = [float(x) for x in column2] # Convert the strings in the column to numbers
    sum_column1 = sum(column) # Adds all the data in the first specified column
    sum_column2 = sum(column2) # Adds all the data in the second specified column
    result =  sum_column1 - sum_column2 # Subtracts both totals
    return result
