#Delete Middle Node: Implement an algorithm to delete a node in the middle of a singly linkedlist(i.e. any node but the first and last node)
#The node hasn't to be the middle node. Access is only given to that node

class Node:
    def __init__(self,dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None


class SLinkedlist:
    def __init__(self) -> None:
        self.headval=None

    def printList(self):
        printlist=self.headval
        while printlist is not None:
            print(printlist.dataval)
            printlist=printlist.nextval
    

    def insertNode(self,newData):
        newNode=Node(newData)
        if self.headval is None:
            self.headval=newNode
            return
        adding=self.headval
        while(adding.nextval is not None):
            adding=adding.nextval
        adding.nextval=newNode

    def insertMiddle(self,key,newData):
        newNode=Node(newData)
        adding=self.headval
        while(adding.nextval is not None):
            if(adding.dataval==key):
                newNode.nextval=adding.nextval
                adding.nextval=newNode
            adding=adding.nextval
    

    def removenode(self,key):
        removing=self.headval
        if(removing is None):
            return
        if(removing.dataval==key):
            self.headval=removing.nextval
            removing=None
            return
        while(removing is not None):
            if(removing.dataval==key):
                break
            remove=removing
            removing=removing.nextval

        remove.nextval=removing.nextval
        removing=None
def removewihouthead(item):
    remove=item.nextval
    item.nextval=remove.nextval
    remove=None

Head=SLinkedlist()
Head.headval=Node("Mon")
node1=Node("Tues")
Head.headval.nextval=node1
node2=Node("Wed")
node1.nextval=node2
node3=Node("Thurs")
node2.nextval=node3
node4=Node("Fri")
node3.nextval=node4
node5=Node("Sat")
node4.nextval=node5
node6=Node("Sun")
node5.nextval=node6
Head.printList()
removewihouthead(node4)
print("-------------")
Head.printList()
