# Step 1
my_list = []

# Step 2: Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3:
my_list.insert(1, 15)

# Step 4: Extending my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Removing the last element from my_list
my_list.pop()

# Step 6: my_list in ascending order
my_list.sort()

# Step 7:
index_of_30 = my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)
