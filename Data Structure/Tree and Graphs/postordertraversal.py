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
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()
        print(self.data)
    
    def postorder(self,root):
        res=[]
        # print(root.data)
        if(root):
            res=self.postorder(root.left)
            res=res+self.postorder(root.right)
            print(root.data)
            res=res.append(root.data)
        return res

Root=Node()
Root.insert(27)
Root.insert(14)
Root.insert(35)
Root.insert(42)
Root.insert(10)
Root.insert(19)
Root.insert(31)
Root.postorder(Root)
# Root.printTree()