from Extra_cost import column_data, sort_data_in_column, sum_of_column

def main():
    non_smokers_gathered = column_data("non_smokers_data.csv", "charges")
    smokers_gathered = column_data("smokers_data.csv", "charges")
    sorted_non_smokers = sort_data_in_column(non_smokers_gathered, smokers_gathered)
    sum_of_both = sum_of_column(smokers_gathered, sorted_non_smokers)

    print(round(sum_of_both / 274, 2))

if __name__ == '__main__':
    main()