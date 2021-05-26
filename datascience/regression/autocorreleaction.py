import pandas as pd
import matplotlib.pyplot as plt
import sklearn

f = pd.read_csv('data/03corr.csv')

f['t0'] = pd.to_numeric(f['t0'], downcast='float')

plt.acorr(f['t0'], maxlags=10)

t_1 = f['t0'].shift(+1).to_frame()
t_2 = f['t0'].shift(+2).to_frame()

print(t_1)

plt.show()
