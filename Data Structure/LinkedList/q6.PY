#palindrome: Implement a function to check if a linked list is in palindrome or not

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
    


    def insertAtBeginning(self,newData):
        newNode=Node(newData)
        newNode.nextval=self.headval
        self.headval=newNode

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


def listreverse(list1):
    dummylist=SLinkedlist()
    pointer1=list1.headval
    while pointer1 is not None:
        dummylist.insertAtBeginning(pointer1.dataval)
        pointer1=pointer1.nextval
    return dummylist

def palindromechecker(list1):
    reversedlist=listreverse(list1)
    pointer1=list1.headval
    reversepointer=reversedlist.headval
    while pointer1 is not None:
        if(pointer1.dataval!=reversepointer.dataval):
            return False
        pointer1=pointer1.nextval
        reversepointer=reversepointer.nextval
    return True

LList=[1,0,0,0,0,0,0,0,1]
Head=SLinkedlist()
for i in LList:
    Head.insertNode(i)
print(palindromechecker(Head))

