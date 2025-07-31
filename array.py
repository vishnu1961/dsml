x=[1,3,5,7,9]
y=[2,5,7,8,9]
add=[a+b for a,b in zip(x,y)]
diff=[a-b for a,b in zip(x,y)]
product=[a*b for a,b in zip(x,y)]
print("addition :",add)
print("difference :",diff)
print("product :",product)

