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
    
    def addNode(self,newdata):
        newNode=Node(newdata)
        if self.headval is None:
            self.headval=newNode
            return
        adding=self.headval
        while(adding.nextval):
            adding=adding.nextval
        adding.nextval=newNode

Head=SlinkedList()
Head.addNode("Monday")
Head.addNode("Tuesday")
Head.addNode("Wednesday")
Head.addNode("Thursday")
Head.addNode("Friday")
Head.addNode("Saturday")
Head.addNode("Sunday")
Head.printlist()


