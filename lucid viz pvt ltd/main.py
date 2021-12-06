import pandas as pd

data = pd.read_csv("in.csv")

print("Median of given data")
print("Median : ",data.median()[0])

print("Mean of given data")
print("Mean : ",data.mean()[0])

print("Standard Deviation of given data")
print("Standard Deviation : ",data.std()[0])