import pandas as pd


insurance_data = pd.read_csv("insurance.csv") # Saves the insurance.csv file

non_smokers_data = insurance_data.loc[insurance_data["smoker"] == "no"] # Saves all data for the smokers column
smokers_data = insurance_data.loc[insurance_data["smoker"] == "yes"] # Saves all data for the smokers column

non_smokers_data.to_csv("non_smokers_data.csv") # Writes the smokers_data to the new csv file
smokers_data.to_csv("smokers_data.csv") # Writes the smokers_data to the new csv file