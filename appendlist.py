mylist = []
num_element = int(input("How many elements do you want to enter? "))
for i in range(num_element):
    element = input(f"Enter element {i+1}: ")
    mylist.append(element)
print("Your list:", mylist)
