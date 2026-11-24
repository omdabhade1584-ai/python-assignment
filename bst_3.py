# Node structure
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def search(root, key):
   
    # root is null -> return false
    if root is None:
        return False

    # if root has key -> return true
    if root.data == key:
        return True

    if key > root.data:
        return search(root.right, key)

    return search(root.left, key)


root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(9)

key = 7
# Searching for key in the BST
print(search(root, key))