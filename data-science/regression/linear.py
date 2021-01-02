import pandas as pd
import sklearn

dataset = pd.read_csv('data/01Students.csv')

df = dataset.copy()

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = \
	train_test_split(X, Y, test_size=0.3, random_state=1234)

from sklearn.linear_model import LinearRegression

std_reg = LinearRegression()

std_reg.fit(x_train, y_train)

y_predict = std_reg.predict(x_test)

slr_score = std_reg.score(x_test, y_test)

slr_coefficient = std_reg.coef_
slr_intercept = std_reg.intercept_

from sklearn.metrics import mean_squared_error
import math

slr_rmse = math.sqrt(mean_squared_error(y_test, y_predict))

import matplotlib.pyplot as plt

plt.scatter(x_test, y_test)

plt.plot(x_test, y_predict)
plt.ylim(ymin=0)

plt.show()
