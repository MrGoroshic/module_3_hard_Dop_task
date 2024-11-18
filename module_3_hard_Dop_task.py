data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(nested_structure):
    count = 0
    if isinstance(nested_structure, (list, tuple, set, dict)):
        if isinstance(nested_structure, dict):
            for key, value in nested_structure.items():
                count += len(key)
                count += calculate_structure_sum(value)
        else:
            iterable = nested_structure.values() if isinstance(nested_structure, dict) else nested_structure
            for element in iterable:
                count += calculate_structure_sum(element)
    elif isinstance(nested_structure, (int, float)):
        count += nested_structure
    elif isinstance(nested_structure, str):
        count += len(nested_structure)
    return count


result = calculate_structure_sum(data_structure)
print(result)