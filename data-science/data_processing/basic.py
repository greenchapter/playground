import pandas as pd
import sklearn

dataset = pd.read_csv('data/loan_small.csv')

subset = dataset.iloc[0:3, 1:3]

subsetN = dataset[['Gender', 'ApplicantIncome']][0:3]

datasetT = pd.read_csv('data/loan_small_tsv.txt', sep='\t')

# print(dataset.head(10))
# print(dataset.shape)
# print(dataset.columns)
# print(dataset.columns[2])
# print(dataset.isnull().sum(axis=0))

# dataset.isnull().sum(axis=0)


# cleandata = dataset.dropna(subset=['Loan_Status'])

dt = dataset.copy()
cols = ['Gender', 'Area', 'Loan_Status']

dt[cols] = dt[cols].fillna(dt.mode().iloc[0])

cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
dt[cols2] = dt[cols2].fillna(dt.mean())
dt.isnull().sum(axis=0)

dt.dtypes

dt[cols] = dt[cols].astype('category')

for columns in cols:
	dt[columns] = dt[columns].cat.codes

df2 = dataset.drop(['Loan_ID'], axis=1)

df2 = pd.get_dummies(df2)



cleandata = dataset.dropna()

data_to_scale = cleandata.iloc[:, 2:5]

from sklearn.preprocessing import StandardScaler

scaler_ = StandardScaler()

ss_scaler = scaler_.fit_transform(data_to_scale)

from sklearn.preprocessing import minmax_scale

mm_scaler = minmax_scale(data_to_scale)


# print(mm_scaler);


dt = dt.drop(['Loan_ID'], axis=1)

dt = pd.get_dummies(dt, drop_first=True)

X = dt.iloc[:, :-1]
Y = dt.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = \
train_test_split(X, Y, test_size=0.15, random_state=1234)

print(x_train)
print(x_test)








