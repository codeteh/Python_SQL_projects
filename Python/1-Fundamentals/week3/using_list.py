states = ["Washington", "Oregon", "California"]

print(states)

print(states[0])
print(states[1])
print(states[2])

print(states[-1])
print(states[-2])
print(states[-3])

# substituting an element in a list
states[2] = "Arizona"
print(states)
print(len(states))

# using appending to adds an element to the end of a list
states.append("New York")
states.append("New Jersey")
states.append("Utah")
print(states)

# removing an element from a list
states.pop()
print(states)
states.pop(4)
print(states)
