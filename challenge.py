import matplotlib.pyplot as plt # Biasanya buat GUI

# x and y axis values
x = [1,2,3,4,5,6,8]
y = [2,4,3,6,5,8,0]

# plotting the points
plt.plot(x,y)

# naming the axis
plt.xlabel('x-axis', fontsize=10)
plt.ylabel('y-axis', fontsize=10)

# labels
plt.text(2,4,'Mulai karir', fontsize=10)
plt.text(4,6,'Karir Meningkat', fontsize=10)
plt.text(6,8,'Gara-gara perempuan', fontsize=10)
plt.text(7,1,'Merosot', fontsize=10)

# Title
plt.title('Graph')


# showing the plot
plt.show()