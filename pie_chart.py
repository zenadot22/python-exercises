import matplotlib.pyplot as plt
sizes=[25,20,45,10]
labels=["cats","dogs","tigers","goats"]

plt.pie(sizes, labels=labels,autopct = "%.2f")
plt.axes().set_aspect("equal")
plt.show()
