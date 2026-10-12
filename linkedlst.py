# class Linkedlist:
#     def delfirst_lst(self):
#         temp=self.head
#         temp1=None
#         prev=None
#         temp.self.head=self.head.next
#         while (temp.next):
#             prev=temp
#             temp=temp.next
#         prev.next=None
#         temp=None
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def delfirst_lst(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    def dellast_lst(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = Linkedlist()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

print("Original list:")
ll.display()

ll.delfirst_lst()
print("After deleting first node:")
ll.display()

ll.dellast_lst()
print("After deleting last node:")
ll.display()

