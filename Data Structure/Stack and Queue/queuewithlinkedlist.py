class Node:
    def __init__(self,dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None


class LinkedList:
    def __init__(self) -> None:
        self.headval=None

    def printList(self):
        printlist=self.headval
        while printlist is not None:
            print(printlist.dataval)
            printlist=printlist.nextval

    def insertnode(self,newData):
        newNode=Node(newData)
        if(self.headval is None):
            self.headval=newNode
            return
        adding=self.headval
        while adding.nextval is not None:
            adding=adding.nextval
        adding.nextval=newNode
    
    def removenode(self):
        removing=self.headval
        if(removing is None):
            return "Queue is empty"
        self.headval=removing.nextval
        item=removing.dataval
        removing=None
        return item
        
    def queueempty(self):
        return self.headval==None
    


queue=LinkedList()
queue.insertnode(1)
queue.insertnode(2)
queue.insertnode(3)
queue.insertnode(4)
queue.insertnode(5)
queue.printList()
print("----------")
print(queue.removenode())
print("----------")
queue.printList()