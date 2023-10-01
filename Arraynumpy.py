# Step1 :install numpy using the command :pip install numpy(In Command Prompt)

import numpy as np

# Creating a NumPy array
my_array = np.array([1, 2, 3, 4, 5])

# Accessing elements
first_element = my_array[0]
print("First element:", first_element)

# Modifying elements
my_array[2] = 10
print("Modified array:", my_array)

# Shape of the array
array_shape = my_array.shape
print("Array shape:", array_shape)

# Adding elements (appending to the end)
# Note: NumPy arrays are fixed in size, so you typically create a new array.
my_array = np.append(my_array, 6)
print("Array after appending:", my_array)

# Removing elements (slicing)
my_array = np.delete(my_array, 1)
print("Array after removal:", my_array)
