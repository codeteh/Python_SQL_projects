state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Salem"}
# print(len(state_capitals))
# print(state_capitals["Washington"])

state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"
print(state_capitals)

del state_capitals["California"]
print(state_capitals)

removed_capital = state_capitals.pop("Oregon")
print(state_capitals)
"""
 difference between del and pop?

 the pop() method returns the value that's being "popped off", so that you can use it if needed. 


"""

print(state_capitals)
print(removed_capital)
