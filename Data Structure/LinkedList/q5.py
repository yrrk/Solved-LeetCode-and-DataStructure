#SumList: You have two number represented by a linkedlist where each node contain a single digit
#The digit are stored in reverse order such that 1's digit is at the head of the list.
#Write a function that add the twoo number & return the sum as linkedList

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
        
def addLists(list1,list2):
    carry=0
    Anslink=SLinkedlist()
    pointer1=list1.headval
    pointer2=list2.headval
    lastNode=False
    while(pointer1 is not None):
        Ans=pointer1.dataval+pointer2.dataval+carry
        if(len(str(Ans))>1):
            if(pointer1.nextval==None):
                lastNode=True
            carry=int(str(Ans)[0])
            Ans=int(str(Ans)[1])
        Anslink.insertNode(Ans)
        pointer1=pointer1.nextval
        pointer2=pointer2.nextval
    if(lastNode):
        Anslink.insertNode(carry)
    return Anslink

    
def padding(list1,list2):
    pointer1=list1.headval
    pointer2=list2.headval
    while(pointer1!=None or pointer2!=None):
        if(pointer1.nextval==None and pointer2.nextval==None):
            return
        if(pointer1.nextval==None or pointer2.nextval==None):
            if(pointer1.nextval==None):
                list1.insertNode(0)
            else:
                list2.insertNode(0)
        pointer1=pointer1.nextval
        pointer2=pointer2.nextval
number1=[7]
number2=[8]
number1Link=SLinkedlist()
number2Link=SLinkedlist()
for i in number1:
    number1Link.insertNode(i)
for i in number2:
    number2Link.insertNode(i)
padding(number1Link,number2Link)
sol=addLists(number1Link,number2Link)
sol.printList()