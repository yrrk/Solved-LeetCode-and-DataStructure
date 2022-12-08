class Node:
    def __init__(self,data=None) -> None:
        self.data=data
        self.left=None
        self.right=None

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
    
    # def printTree(self):
    #     if(self.left):
    #         self.left.printTree()
    #     print(self.data)
    #     if(self.right):
    #         self.right.printTree()


    def printTree(self):
        print(self.data)
        if(self.left):
            self.left.printTree()
        if(self.right):
            self.right.printTree()
    
    def preorderTraversal(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.preorderTraversal(root.left)
            res=res+self.preorderTraversal(root.right)
        return res



Root=Node()
Root.insert(27)
Root.insert(35)
Root.insert(14)
Root.insert(42)
Root.insert(19)
Root.insert(10)
Root.insert(31)

print(Root.preorderTraversal(Root))
Root.printTree()