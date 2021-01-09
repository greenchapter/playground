from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris.data
Y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
	train_test_split(X, Y, test_size=0.3, random_state=1234, stratify=Y)

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

svc = SVC(kernel='rbf', gamma=1.7)
svc.fit(x_train, y_train)
Y_predict = svc.predict(x_test)
cm_rbf01 = confusion_matrix(y_test, Y_predict)

print(cm_rbf01)

svc = SVC(kernel='rbf', gamma=10.0)
svc.fit(x_train, y_train)
Y_predict = svc.predict(x_test)
cm_rbf10 = confusion_matrix(y_test, Y_predict)

svc = SVC(kernel='poly')
svc.fit(x_train, y_train)
Y_predict = svc.predict(x_test)
cm_poly = confusion_matrix(y_test, Y_predict)

svc = SVC(kernel='sigmoid')
svc.fit(x_train, y_train)
Y_predict = svc.predict(x_test)
cm_sigmoid = confusion_matrix(y_test, Y_predict)

svc = SVC(kernel='linear')
svc.fit(x_train, y_train)
Y_predict = svc.predict(x_test)
cm_linear = confusion_matrix(y_test, Y_predict)




formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])


# plt.figure(figsize=(5, 4))
# plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
# plt.colorbar(ticks=[0, 1, 2], format=formatter)
# plt.xlabel(iris.feature_names[0])
# plt.ylabel(iris.feature_names[1])

# plt.figure(figsize=(5, 4))
# plt.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target)
# plt.colorbar(ticks=[0, 1, 2], format=formatter)
# plt.xlabel(iris.feature_names[2])
# plt.ylabel(iris.feature_names[3])

fig = plt.figure("My Default Figure", dpi=72, facecolor='w', edgecolor='k')

ax = fig.add_subplot(1, 2, 1)
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
# fig.colorbar(ax)
ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)

ax1 = fig.add_subplot(1, 2, 2)
ax1.set_xlabel(iris.feature_names[2])
ax1.set_ylabel(iris.feature_names[3])
# ax.colorbar(ticks=[0, 1, 2], format=formatter)
ax1.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target)


# fig.colorbar()

plt.tight_layout()
plt.show()
