# Simple lambda Expression

add = lambda x, y: x + y
result = add(5, 3)
print(result)

# Simple lambda Expression with Collections(List)

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
result = list(squared)
print(result)


# Simple lambda Expression with Filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
result = list(even_numbers)
print(result)


# Simple lambda Expression with Sorting

students = [
    {"name": "Maya", "score": 90},
    {"name": "Naren", "score": 85},
    {"name": "Charlie", "score": 95},
]

sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)
