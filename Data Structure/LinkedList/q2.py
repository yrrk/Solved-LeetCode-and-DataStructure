#Return Kth to last: Implement an algorithm to find the kth to the last element of a singly linked list

from typing import Counter


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

#This is the implementation for this question
    def returnKelement(self,key):
        pointer1=self.headval
        kpointer=self.headval
        counter=0
        while pointer1 is not None:
            pointer1=pointer1.nextval
            counter+=1
            if(counter>key):
                kpointer=kpointer.nextval
        print(kpointer.dataval)



Head=SLinkedlist()
Head.insertNode("Mon")
Head.insertNode("Tue")
Head.insertNode("Wed")
Head.insertNode("Thur")
Head.insertNode("Fri")
Head.insertNode("Sat")
Head.insertNode("Sun")

Head.returnKelement(1)