import matplotlib.pyplot as plt
from collections import Counter

fig = plt.figure("My Default Figure", dpi=72, facecolor='w', edgecolor='k')

# My Chart Plot
x_days = [1, 2, 3, 4, 5]

y_price1 = [9, 9.5, 10.1, 10, 12]
y_price2 = [11, 12, 10.5, 11.5, 12.5]

ax1 = fig.add_subplot(2, 3,  1)
ax1.title.set_text("Stock Movement")
ax1.set_xlabel("Weekdays")
ax1.set_ylabel("Price in USD")
ax1.plot(x_days, y_price1, label="Stock 1", color='green', marker='o', markersize=5, linewidth=2, linestyle='--')
ax1.plot(x_days, y_price2, label="Stock 2")
ax1.legend(loc=2, fontsize=9)
ax1.figure.savefig("plots/chart.pdf", bbox_inches="tight")



# Bar Plot
x_cities = ["New York", "London", "Dubai", "New Dehli", "Tokyo"]
y_temp = [75, 65, 105, 98, 90]

ax2 = fig.add_subplot(2, 3,  2)
ax2.title.set_text("Temperature Variations")
ax2.set_xlabel("Cities")
ax2.set_ylabel("Temperature")
ax2.set_xticks(range(len(x_cities)))
ax2.set_xticklabels(x_cities, rotation='45', size=9)
ax2.bar(x_cities, y_temp)
ax2.figure.savefig("plots/bar.pdf", bbox_inches="tight")



# Histogram Plot
f = open("data/agedata.csv", "r")
agefile = f.readlines()
age_list = []

for records in agefile:
	age_list.append(int(records))

bins = [10, 20, 30, 40, 50, 60, 70 ,80 ,90, 100]

ax3 = fig.add_subplot(2, 3,  3)
ax3.title.set_text("Age Histogram")
ax3.set_xlabel("Group")
ax3.set_ylabel("Age")
ax3.hist(age_list, bins, histtype='bar', rwidth=0.9)
ax3.figure.savefig("plots/histogram.pdf", bbox_inches="tight")



# Box Plot
f = open("data/salesdata.csv", "r")
salefile = f.readlines()
sale_list = []

for records in salefile:
	sale_list.append(int(records))

ax4 = fig.add_subplot(2, 3,  4)
ax4.title.set_text("Boxplot of Sales")
ax4.boxplot(sale_list)
ax4.figure.savefig("plots/box.pdf", bbox_inches="tight")



# Pie Plot
f = open("data/agedata2.csv", "r")
agefile = f.readlines()
city_list = []

for records in agefile:
	age, city = records.split(sep=',')
	city_list.append(city)

city_count = Counter(city_list)
city_names = list(city_count.keys())
city_values = list(city_count.values())

ax5 = fig.add_subplot(2, 3, 5)
ax5.pie(city_values, labels=city_names, autopct='%.4f%%')
ax5.figure.savefig("plots/pie.pdf", bbox_inches="tight")



# Scatter Plot
f = open("data/salesdata2.csv", "r")
salefile = f.readlines()

s_list = []
c_list = []

for records in salefile:
	sale, cost = records.split(sep=',')
	s_list.append(int(sale))
	c_list.append(int(cost))

ax6 = fig.add_subplot(2, 3, 6)
ax6.title.set_text("Sales vs Cost")
ax6.set_xlabel("Sale")
ax6.set_ylabel("Cost")
ax6.scatter(s_list, c_list, marker='*', s=100, c='#FF5733')
ax6.figure.savefig("plots/scatter.pdf", bbox_inches="tight")



plt.tight_layout()
plt.savefig("plots/full.png")
plt.show()
