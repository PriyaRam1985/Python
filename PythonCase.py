def switch_case(argument):
    switch = {
        "case1": "This is case 1",
        "case2": "This is case 2",
        "case3": "This is case 3",
    }
    return switch.get(argument, "This is the default case")

# Example usage
result = switch_case("case2")
print(result)

result = switch_case("case4")  # Using the default case
print(result) 
