import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#reading data file 
df=pd.read_excel("C:/Users/Abhi/Desktop/problem/real_state.xlsx")
print(df.head())
df=df.rename(columns={"X1 transaction date":"X1","X2 house age":"X2","X3 distance to the nearest MRT station":"X3","X4 number of convenience stores":"X4","X5 latitude":"X5","X6 longitude":"X6","Y house price of unit area":"Y"})

print(df.head())
#checking the dataset
print(df.isnull())
print(df.duplicated())
print(df.count())
print(df.dtypes)
print(df.describe())

#remove useless column "NO" 
df=df.drop("No",axis=1)
print(df.head())
#seperating the labes from the dataset
Y=df["Y"]
#drop the label column from dataset
df=df.drop("Y",axis=1)
print(df.head())
print(Y.head())


x_train,x_test,y_train,y_test=train_test_split(df,Y,random_state=1)
#rescaling the data 
scaler=StandardScaler()
scaler.fit(x_train)
x_train_scaled=scaler.transform(x_train)
x_test_scaled=scaler.transform(x_test)



