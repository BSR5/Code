import pandas as pd


insurance_data = pd.read_csv("insurance.csv")

non_smokers_data = insurance_data.loc[insurance_data["smoker"] == "no"]
smokers_data = insurance_data.loc[insurance_data["smoker"] == "yes"]

non_smokers_data.to_csv("non_smokers_data.csv")
smokers_data.to_csv("smokers_data.csv")