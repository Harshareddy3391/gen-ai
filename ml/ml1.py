from sklearn.linear_model import LinearRegression
import numpy as np



x=np.array([[1],[2],[3],[4]])
y=np.array([20,40,60,80])

model=LinearRegression()
model.fit(x,y)


d=model.predict([[8]])

print(d)