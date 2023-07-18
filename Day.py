import matplotlib.pyplot as plt

a = [1,2,3,4,5]
b = [0, 0.6, 0.2, 15, 10, 8,16,21]
plt.plot(a)

# o is for circle and r for red
plt.plot(b, "or")

plt.plot(list(range(0,22,3)))

plt.xlabel("Day ->")
plt.ylabel("Temp ->")

c = [4,2,6,8,3,20,13,15]
plt.plot(c,label="4th rep")

ax = plt.gca()

# get command over the individual boundary of the graph body
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# set the range of bounds of left
ax.spines["left"].set_bounds(-3,40)

# set the interval in x-axis and y-axis
plt.xticks(list(range(-3,10)))
plt.yticks(list(range(-3,20,3)))

# Legend
ax.legend(["1st rep", "2nd rep", "3rd rep", "4th rep"])

# anotate command helps to write on the graphs at any xy denotes
plt.annotate("Temperature V/s Days", xy=(1.01, -2.15))

# Title
plt.title("Day - Temperature Line Graph")

plt.show()