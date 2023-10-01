#List Comprehensions:
#new_list = [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)


#Dictionary Comprehension
#new_dict = {key_expression: value_expression for item in iterable if conditionnames = ['Alice', 'Bob', 'Charlie']

names=['Sachin','singh']
name_lengths = {name: len(name) for name in names}
print(names)


#Set Comprehension
#new_set = {expression for item in iterable if condition}

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)
