class Node:
    def __init__(self,dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None

class SlinkedList:

    def __init__(self) -> None:
        self.headval=None
    
    def printlist(self):
        printlist=self.headval
        while printlist is not None:
            print(printlist.dataval)
            printlist=printlist.nextval

    def addinmiddle(self,middlenode,newdata):
        if middlenode is None:
            print("The middle node is absent")
            return

        newNode=Node(newdata)
        newNode.nextval=middlenode.nextval
        middlenode.nextval=newNode



head=SlinkedList()
head.headval=Node("Mon")
e2=Node("Tuesday")
head.headval.nextval=e2
e3=Node("Wednesday")
e2.nextval=e3
e4=Node("Friday")
e3.nextval=e4
e5=Node("Saturday")
e4.nextval=e5

head.addinmiddle(e3,"Thursday")
head.printlist()