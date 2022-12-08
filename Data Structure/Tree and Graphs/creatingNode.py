class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    
    def printTree(self):
        print(self.data)



Root=Node(5)
Root.printTree()