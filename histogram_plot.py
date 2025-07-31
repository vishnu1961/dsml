import matplotlib.pyplot as plt
data = [55, 67, 89, 45, 56, 78, 67, 90, 45, 67, 85, 70, 60, 75, 88]
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
