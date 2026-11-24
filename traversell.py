class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(40)
head.next.next = Node(70)

temp = head

while temp is not None:
    print(temp.data)
    temp = temp.next
