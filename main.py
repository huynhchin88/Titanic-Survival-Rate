import pandas as pd

#load data
data = pd.read_csv("dataset/train.csv")

#view first few rows
print(data.head())
#check for missing data
print(data.isnull().sum())