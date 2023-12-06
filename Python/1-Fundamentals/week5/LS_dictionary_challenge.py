
def linear_search_dictionary(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            return key
    return None




my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
result1 = linear_search_dictionary(my_dictionary, 5)
result2 = linear_search_dictionary(my_dictionary, 3)
result3 = linear_search_dictionary(my_dictionary, 8)


if result1 is not None:
    print(f"Found at {result1}")
else:
    print(f"Target is not found in dictionary")

if result2 is not None:
    print(f"Found at {result2}")
else:
    print(f"Target is not found in dictionary")

if result3 is not None:
    print(f"Found at {result3}")
else:
    print(f"Target is not found in dictionary")