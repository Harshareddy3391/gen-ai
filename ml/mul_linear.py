from sklearn.linear_model import LinearRegression
import numpy as np


a=np.array([[1],[2],[3],[4]])
b=np.array([20,40,60,80])


model=LinearRegression()

model.fit(a,b)
  

c=model.predict([[8]])

print(c)
print(a)
print(b)
