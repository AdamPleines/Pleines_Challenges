# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(LL):  
    LL.head = None

# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LinkedList)