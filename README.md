US Medical Insurance Project  
By Ben Martinez  

Project Overview:  
In this project, I will be using python to analyse a dataset provided by Codecademy containing information about 1338 people in the US including their; age, sex, BMI, number of children, smoking status, region and the prices of their medical insurance coverage. I will create a python program to analyse this data and estimate how much extra the people in this dataset are paying for their medical insurance based on whether they smoke.

Objectives:
- Find out how much the cost of medical insurance increases when smoking  
- Use functions to gather and analyse the data from the provided sheet  
- Write a short conclusion explaining my findings    

Outline of what needs to be done:  
First, we need to get the data from the CSV file provided by Codecademy. Then, we need to clean the data to acquire what we need to analyse the smoker’s information. After, we need to create functions to separate out the information needed to analyse smoker’s data. Next, we need to create different functions to calculate the data required to carry out our objectives.

In-depth file explanation  
Insurance.csv:  
This contains all of the data that Codecademy wants us to analyse, including the age (integer), sex (string), BMI (float), number of children (integer), smoking status (Boolean), region (string) and charges (float). This file contains the data for 1338 people.
-	The "age" column contains the age of all the people included.
-	The "sex" column contains the gender of the people included.
-	The "bmi" column contains the peoples BMI measurement.
-	The "children" column contains the number of children each person has.
-	The "smoker" column contains weather the people smoke.
-	The "region" column contains region people are from.
-	The "charges" column contains the values of each person’s actual medical insurance costs.

creates_csv_file.py:   
The Python code uses the Pandas library to load a CSV file called “insurance.csv” and save it as a Pandas DataFrame object in the variable `insurance_data`. Then, it uses the DataFrame's `.loc[]` method to filter the data based on the values in the `smoker` column. It saves the data for non-smokers in the `non_smokers_data` variable and the data for smokers in the `smokers_data` variable. Finally, it writes these two filtered DataFrames to two new CSV files called [[non_smokers_data.csv]] and [[smokers_data.csv]].

non_smokers_data.csv  
This CSV file contains all of the data for the people who *DO NOT* smoke. The data inside this csv file was taken from the `insurance.csv` data using the above describes `creates_csv_file.py` program. Below is what the first 5 rows look like in the file:
-	,age,sex,bmi,children,smoker,region,charges
-	1,18,male,33.77,1,no,southeast,1725.5523
-	2,28,male,33.0,3,no,southeast,4449.462
-	3,33,male,22.705,0,no,northwest,21984.47061
-	4,32,male,28.88,0,no,northwest,3866.8552
-	5,31,female,25.74,0,no,southeast,3756.6216  

smokers_data.csv  
This CSV file contains all of the data for the people who *DO* smoke. The data inside this csv file was taken from the `insurance.csv` data using the above describes `creates_csv_file.py` program. Below is what the first 5 rows of data look like:
-	,age,sex,bmi,children,smoker,region,charges
-	0,19,female,27.9,0,yes,southwest,16884.924
-	11,62,female,26.29,0,yes,southeast,27808.7251
-	14,27,male,42.13,0,yes,southeast,39611.7577
-	19,30,male,35.3,0,yes,southwest,36837.467
-	23,34,female,31.92,1,yes,northeast,37701.8768

Extra_cost.py  
The code imports the pandas library, which is a popular Python library for data analysis and manipulation. It then defines three functions: `column_data()`,`sort_data_in_column()`, and `sum_of_column()`. The `column_data()` function takes in a “file_name” and a “column_name” as arguments and returns a column of data from the specified file. The `sort_data_in_column()` function takes in two columns of data and returns the first column sorted in descending order and limited to the length of the second column. Finally, the `sum_of_column()` function takes in two columns of data and returns the difference between the sum of the first column and the sum of the second column.

Main.py   
This code imports the functions from the "Extra_costs.py" file and then uses them in a new function to read the data from "non_smokers_data.csv" and "smokers_data.csv". Then it extract the "charges" column from each file, sorts the data in the "charges" column from the "non_smokers_data.csv" file and calculates the difference between the sum of the "charges" column from the "smokers_data.csv" file and the sorted "charges" column from the "non_smokers_data.csv" file. The result is then divided by 274, rounded to the nearest 2 decimal places and printed. The final if statement is used to call the `main()` function to display the result in the terminal.

Conclusion  
The result of the above program shows that on average, it will cost a person who smokes $15,865.00 more than if they were to not smoke. That would be a MAJOR saving that I’m sure would motivate the majority of the people who do smoke in this data to quit.

Link to the project:   
https://github.com/BSR5/Code
