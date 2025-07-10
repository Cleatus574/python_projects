import pandas as pd
import numpy as np
import scipy

data = pd.read_csv("/Users/ianedgecomb/hmdacodes_me_2017.csv", delimiter=",")
print(data.head())
# list_of_column_names = list(data.columns)
# print(list_of_column_names)
# mean_all = data["loan_amount_000s"].mean()
# print(mean_all)
# Create new pandas DataFrame
hmda = data[
    [
        "loan_type",
        "loan_purpose",
        "owner_occupancy",
        "loan_amount_000s",
        "action_taken",
        "msamd",
    ]
]
# print(hmda)
print(hmda.columns)
# return the standard deviation of loan amounts
# stdev = hmda['loan_amount_000s'].std()
# print(stdev)

# return the 75th percentile for loan amount
