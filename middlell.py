class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(5)
head.next.next = Node(7)
head.next.next.next = Node(13)
head.next.next.next.next = Node(19)

slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print("Middle node:", slow.data)