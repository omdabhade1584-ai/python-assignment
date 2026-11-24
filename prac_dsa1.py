
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list (append nodes)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print node values
    def display(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert node at a specific position
    def insert(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete nodes having negative values
    def delete_negative(self):
        # Delete negative nodes from the beginning
        while self.head is not None and self.head.data < 0:
            self.head = self.head.next

        # Delete negative nodes from the remaining list
        temp = self.head

        while temp is not None and temp.next is not None:
            if temp.next.data < 0:
                temp.next = temp.next.next
            else:
                temp = temp.next



ll = LinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = float(input("Enter positive or negative number: "))
    ll.append(value)

print("\nOriginal Linked List:")
ll.display()

data = int(input("\nEnter value to insert: "))
position = int(input("Enter position: "))

ll.insert(data, position)

print("\nLinked List after insertion:")
ll.display()

ll.delete_negative()

print("\nLinked List after deleting negative nodes:")
ll.display()