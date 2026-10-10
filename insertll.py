class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

data = int(input("Enter data: "))
pos = int(input("Enter position: "))

new_node = Node(data)

if pos == 1:
    new_node.next = head
    head = new_node
else:
    temp = head
    for i in range(pos - 2):
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node

temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
