import matplotlib.pyplot as plt # Biasanya buat GUI

a=2
b=3

# x and y axis values
x = ["1","2"]
y = [a,b]

# plotting the points
plt.plot(x,y)

# naming the axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Title
plt.title('My First Graph')


# showing the plot
plt.show()

