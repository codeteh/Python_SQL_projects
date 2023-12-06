""" This creates a Node class that contains a value 
and reference (link) to the 
next value, initially set to None. None is 
a special value in Python that explicitly denotes 
the intentional lack of any value.  """


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)
print(head.next.value)
print(head.next.next.value)
