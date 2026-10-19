#Delete the node in Dobly Linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        temp = self.head
        # Find the node
        while temp and temp.data != value:
            temp = temp.next
        if temp is None:
            print("Node not found")
            return
        # Delete the first node
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next
        # Update the next node's prev pointer
        if temp.next:
            temp.next.prev = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Main program
ll = DoublyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Before deletion:")
ll.display()

ll.delete(10)

print("After deletion:")
ll.display()