# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List: ", my_list)

# Step 3: Insert 15 at the second position
my_list.insert(1, 15)
print("Updated list: ", my_list)

# Step 4: Extend the list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print("Extended list: ", my_list)

# Step 5: Remove the last element from the list
my_list.pop()
print("List after removing last element: ", my_list)

# Step 6: Sort the list in ascending order
my_list.sort()
print("Sorted list: ", my_list)

# Step 7: Find and print the index of 30
index = my_list.index(30)
print("Index of 30: ", index)