import matplotlib.pyplot as plt
categories=['apple','banana','cherries','dates']
values=[40,25,30,10]
plt.bar(categories,values,color='orange')
plt.title("fruit sales")
plt.xlabel("fruits")
plt.ylabel("quantity sold")
plt.show()