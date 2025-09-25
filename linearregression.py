from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets,linear_model
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score
df=pd.read_csv("data.csv.csv")
x=df[["Weight","Volume"]] 
y=df[['CO2']]
x=x.values
y=y.values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(x_train)
print(y_train)
regr=linear_model.LinearRegression()
regr.fit(x_train,y_train)
predictedCO2=regr.predict([[2300,1300]])
print(predictedCO2)