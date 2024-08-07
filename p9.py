import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Pgm 9-position_salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

def viz_linear():
 plt.scatter(X, y, color='red')
 plt.plot(X, lin_reg.predict(X), color='blue')
 plt.title('Truth or Bluff (Linear Regression)')
 plt.xlabel('Position level')
 plt.ylabel('Salary')
 plt.show()
 return
viz_linear()

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

def viz_polymonial():
 plt.scatter(X, y, color='red')
 plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
 plt.title('Truth or Bluff (Linear Regression)')
 plt.xlabel('Position level')
 plt.ylabel('Salary')
 plt.show()
 return
viz_polymonial()

def viz_polymonial_smooth():
 X_grid = np.arange(min(X), max(X), 0.1)
 X_grid = X_grid.reshape(len(X_grid), 1) #Why do we need to reshape?
 # Visualizing the Polymonial Regression results
 plt.scatter(X, y, color='red')
 plt.plot(X_grid, pol_reg.predict(poly_reg.fit_transform(X_grid)), color='blue')
 plt.title('Truth or Bluff (Linear Regression)')
 plt.xlabel('Position level')
 plt.ylabel('Salary')
 plt.show()
 return
viz_polymonial_smooth()

lin_reg.predict([[5.5]])

pol_reg.predict(poly_reg.fit_transform([[5.5]]))