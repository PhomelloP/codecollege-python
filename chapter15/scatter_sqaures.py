import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-v0_8')
# fig, ax= plt.subplots()
# ax.scatter(x_values, y_values, s=100)

# #Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value",fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# #Set size of tick labels.
# ax.tick_params(labelsize=14)

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values ,y_values, c=(0,0.8,0), s=10)

#Set Chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

#Set size of tick labels.
ax.tick_params(axis= 'both', which='major',labelsize=14)

#Set the range for each axis
ax.axis([0,1100,0,110000])


plt.show()