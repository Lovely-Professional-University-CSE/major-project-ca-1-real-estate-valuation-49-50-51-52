import pandas as pd
import matplotlib.pyplot as plt 
%matplotlib inline
df=pd.read_excel("C:/Users/Abhi/Desktop/problem/real_state.xlsx")
print(df.head())
df=df.rename(columns={"X1 transaction date":"X1","X2 house age":"X2","X3 distance to the nearest MRT station":"X3","X4 number of convenience stores":"X4","X5 latitude":"X5","X6 longitude":"X6","Y house price of unit area":"Y"})

print(df.head())
print(df.isnull())
print(df.duplicated())
print(df.count())
print(df.dtypes)
print(df.describe())
df=df.drop("No",axis=1)
print(df.head())
Y=df["Y"]
df=df.drop("Y",axis=1)
print(df.head())
print(Y.head())

