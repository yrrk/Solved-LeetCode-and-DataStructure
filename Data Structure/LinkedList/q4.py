#Partition:Write a code to partition a linkedlist around a value X, such that all nodes less than X come before all node greater than or equal x.
#If X is contained within the list, the value of X only need to be after the element less than X
from turtle import right


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


def partition(key,mainlist):
    left=SLinkedlist()
    right=SLinkedlist()
    pointer=mainlist.headval
    while(pointer is not None):
        if(pointer.dataval>=key):
            right.insertNode(pointer.dataval)
        else:
            left.insertNode(pointer.dataval)
        pointer=pointer.nextval
    pointer=left.headval
    while(pointer.nextval is not None):
        pointer=pointer.nextval
    pointer.nextval=right.headval
    return left





l1=[3,5,8,5,10,2,1]

Head=SLinkedlist()
for i in l1:
    Head.insertNode(i)
Head=partition(5,Head)
Head.printList()
