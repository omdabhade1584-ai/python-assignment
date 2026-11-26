#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.rt = None
        self.lcnt=0
       
    def insert(self, new_node):
        if self.rt is None: ##BST is empty
            self.rt=new_node
        else:
            temp=self.rt
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def del_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left,val)
        elif val > rt.data:
            rt.right=self.del_node(rt.right,val)

        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.del_node(rt.right, succ.data)
            return rt
    def get_successor(self, temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp
    def search(self, key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key < temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False


    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.lcnt+=1
            self.lcnt+=1
            self.inorder(rt.right)

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
            return
        arr=[]
        cnt=0
        while cnt<len(arr):
            temp=arr[cnt]
            cnt+=1
            print(temp.data, end=" ")
            if temp.left:
                arr.apppend(temp.left)
            if temp.right:
                arr.append(temp.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findminmax(self):
        temp=self.rt
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=self.rt
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)

    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(500))
b1.insert(Node(2))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(75))
b1.insert(Node(250))
b1.insert(Node(50))
print("\nInorder: ")
b1.inorder(b1.rt)
print("\nNo of left nodes: ",b1.lcnt)
print("\nPreorder: ")
b1.preorder(b1.rt)
print("\nPostorder: ")
b1.postorder(b1.rt)
# b1.findminmax()
# b1.del_node(b1.root, 75)
# print("\n After Deletion:",end=" ")
# b1.inorder(b1.root)
b1.level_order(b1.rt)