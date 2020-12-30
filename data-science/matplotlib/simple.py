import matplotlib.pyplot as plt
import numpy as np


x_values = [1, 2, 3, 4]
y_values = [1, 4, 2, 3]

plt.figure("Table")
plt.title("My Values")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x_values, y_values)
plt.savefig("plots/table.png")

plt.figure("Scatter")
plt.title("My scattered values")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x_values, y_values)
plt.savefig("plots/scatter.png")

plt.show()
