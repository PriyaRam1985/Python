# Creating an array-like structure using a list
my_array = [1, 2, 3, 4, 5]
print(my_array)

# Accessing elements
first_element = my_array[0]
print("First element:", first_element)

# Modifying elements
my_array[2] = 10
print("Modified array:", my_array)

# Length of the array
array_length = len(my_array)
print("Array length:", array_length)

# Adding elements (appending to the end)
my_array.append(6)
print("Array after appending:", my_array)

# Removing elements
removed_element = my_array.pop(1)
print("Removed element:", removed_element)
print("Array after removal:", my_array)
