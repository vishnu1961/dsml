import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
bubble_size = [100, 300, 500, 200, 400]
plt.scatter(x, y, s=bubble_size, color='skyblue', alpha=0.6, edgecolors='black')
plt.title("Simple Bubble Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
