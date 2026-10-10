class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

pos = int(input("Enter position to delete: "))

if pos == 1:
    head = head.next
else:
    temp = head
    for i in range(pos - 2):
        temp = temp.next

    temp.next = temp.next.next

temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")