#inorder traversal
class Node:
    def __init__(self,data=None) -> None:
        self.data=data
        self.right=None
        self.left=None

    def insert(self,data):
        newNode=Node(data)
        if(self.data):
            if(data<self.data):
                if(self.left is None):
                    self.left=newNode
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.right is None):
                    self.right=newNode
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def printTree(self):
        if(self.left):
            self.left.printTree()
        print(self.data)
        if(self.right):
            self.right.printTree()


    def inordertraversal(self,root):
        res=[]
        if(root):
            res=self.inordertraversal(root.left)
            res.append(root.data)
            res=res+self.inordertraversal(root.right)
        return res
    

Root=Node()
Root.insert(27)
Root.insert(14)
Root.insert(35)
Root.insert(19)
Root.insert(31)
Root.insert(10)
Root.insert(42)
print(Root.inordertraversal(Root))
Root.printTree()