class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Display
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Insert at position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for i in range(position - 2):
            if current is None:
                print("Invalid position")
                return

            current = current.next

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        current.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    # Search
    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True

            current = current.next

        return False

    # Count nodes
    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# Create Linked List
ll = LinkedList()

# Insert
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print("Linked List:")
ll.display()

# Insert at beginning
ll.insert_beginning(5)

print("After inserting 5 at beginning:")
ll.display()

# Insert at position
ll.insert_position(15, 3)

print("After inserting 15 at position 3:")
ll.display()

# Delete beginning
ll.delete_beginning()

print("After deleting beginning:")
ll.display()

# Delete end
ll.delete_end()

print("After deleting end:")
ll.display()

# Search
print("Search 20:", ll.search(20))

# Length
print("Length:", ll.length())



# 