#Insertion for a Binary Search Tree
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


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if(self.right):
            self.right.printTree()
            
Root=Node()
Root.insert(8)
Root.insert(4)
Root.insert(6)
Root.insert(2)
Root.insert(10)
Root.insert(20)
Root.printTree()
