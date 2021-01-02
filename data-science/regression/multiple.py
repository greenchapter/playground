import pandas as pd
import sklearn

dataset = pd.read_csv('data/02Students.csv')
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

mlr_score = std_reg.score(x_test, y_test)
mlr_coefficient = std_reg.coef_
mlr_intercept = std_reg.intercept_

from sklearn.metrics import mean_squared_error
import math

mlr_rmse = math.sqrt(mean_squared_error(y_test, y_predict))
