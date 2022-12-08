class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None


class SlinkedList:
    def __init__(self):
        self.headval=None

    def printLinkedList(self):
        printlist=self.headval
        while printlist is not None:
            print(printlist.dataval)
            printlist=printlist.nextval

    def Atbeginning(self,newdata):
        newNode=Node(newdata)
        newNode.nextval=self.headval
        self.headval=newNode



Head=SlinkedList()
Head.headval=Node("Mon")
Node1=Node("Tue")
Head.headval.nextval=Node1
Node2=Node("Wed")
Node1.nextval=Node2
Node3=Node("Thurs")
Node2.nextval=Node3
Head.Atbeginning("Sun")
print(Head.headval.dataval)


