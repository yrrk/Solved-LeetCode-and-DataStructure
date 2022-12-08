class Node:

    def __init__(self,dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None
    
   


class Slinkedlist:
    def __init__(self) -> None:
        self.headval=None

    def printlinkedlist(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    


Node1=Slinkedlist()
Node1.headval=Node("Mon")
Node2=Node("Tue")
Node1.headval.nextval=Node2
Node3=Node("Wed")
Node2.nextval=Node3
Node4=Node("Thur")
Node3.nextval=Node4
Node5=Node("Fri")
Node4.nextval=Node5
Node6=Node("Sat")
Node5.nextval=Node6
Node7=Node("Sun")
Node6.nextval=Node7



Node1.printlinkedlist()


