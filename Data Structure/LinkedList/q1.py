#Remove Dups: Write a code to remove duplicate from an Unsorted Linked List
#How would you solve this problem if a temporary buffer is not allowed

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

    def returnDups(self):
        removelist=self.headval
        dupHash={}
        while removelist is not None:
            if(removelist.dataval in dupHash.keys()):
                self.removenode(removelist.dataval)
            dupHash[removelist.dataval]=False
            removelist=removelist.nextval
        
    

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





Head=SLinkedlist()
Head.insertNode("mon")
Head.insertNode("tue")
Head.insertNode("wed")
Head.insertNode("mon")
Head.insertNode("thur")
Head.insertNode("fri")
Head.insertNode("fri")
Head.insertNode("sat")
Head.insertNode("sun")
Head.insertNode("sat")
Head.printList()
Head.returnDups()
print("----------------")
Head.printList()
