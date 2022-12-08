class Node:
    def __init__(self,key=None,data=None) -> None:
        self.data=data
        self.key=key
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.headval=None
    
    def insertNode(self,key,data):
        newNode=Node(key,data)
        if self.headval is None:
            self.headval=newNode
            return
        adding=self.headval
        while adding.next is not None:
            adding=adding.next
        adding.next=newNode
    
    def printHash(self):
        printing=self.headval
        while printing is not None:
            print(printing.key,printing.data)
            printing=printing.next

    def get(self,key):
        getting=self.headval
        while getting is not None:
            if(getting.key==key):
                return getting.data
            getting=getting.next


Hash1=LinkedList()
Hash1.insertNode('yaksh',30)
Hash1.insertNode('sanket',20)
Hash1.insertNode('namrata',40)
Hash1.insertNode('devanshi',50)
print(Hash1.get('yaksh'))