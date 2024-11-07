# an empty list
lengalei_list = []

# Append the elements 10, 20, 30, 40
lengalei_list.append(10)
lengalei_list.append(20)
lengalei_list.append(30)
lengalei_list.append(40)

# Insert the value 15 at the second position
lengalei_list.insert(1, 15)

# Extend lengalei_list with another list [50, 60, 70]
lengalei_list.extend([50, 60, 70])

# Remove the last element from lengalei_list
lengalei_list.pop()

# Sort lengalei_list in ascending order
lengalei_list.sort()
print(lengalei_list)

# Find and print the index of the value 30
index_of_30 = lengalei_list.index(30)
print("The index of 30 in lengalei_list is:", index_of_30)
