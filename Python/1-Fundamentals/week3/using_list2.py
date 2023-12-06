# using for loop with a list

states = [
    "Washington",
    "Oregon",
    "California",
    "New York",
    "New Jersey",
    "Utah",
    "Maryland",
    "Kentucky",
]

"""
for x in states:
    print(x)
"""
"""
for state in states:
    state = state.upper()
    print(state)

print("Washington" in states)
print("Florida" in states)
print("California" not in states)
"""
# concatenating list
states2 = ["Florida", "Texas", "Nevada", "Virginia"]
best_states = states + states2
print(best_states)

# slicing a list
print(best_states[2:5])
print(best_states[:4])
print(best_states[3:])
