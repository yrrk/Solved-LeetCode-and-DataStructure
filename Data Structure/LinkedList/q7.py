#Intersection: Given two singly linked list, determine if the two lists intersect.
#Return the intersecting node and note that the intersection is defined based on reference and not by value
#That is the kth node of the first linked list is the exact same node as the jth node of the second linked list, then they are intersecting
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
    
    def insertatBeginning(self,newData):
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

def intersectinglist(list1,list2):
    pointer1=list1.headval
    while pointer1.nextval is not None:
        pointer1=pointer1.nextval
    pointer1.nextval=list2.headval
    list2.insertatBeginning(10)
    list2.insertatBeginning(11)
    list2.insertatBeginning(12)
    list2.insertatBeginning(13)
    list2.insertatBeginning(14)
    list2.insertatBeginning(16)
    list2.insertatBeginning(17)
    list2.insertatBeginning(18)



def detecting(list1,list2):
    pointer1=list1.headval
    pointer2=list2.headval
    l1len=1
    l2len=1
    while pointer1.nextval is not None:
        l1len+=1
        pointer1=pointer1.nextval
    while pointer2.nextval is not None:
        l2len+=1
        pointer2=pointer2.nextval
    if(pointer1!=pointer2):
        return False
    diff=0
    pointer1=list1.headval
    pointer2=list2.headval
    if(l1len>l2len):
        diff=l1len-l2len
        counter=0
        while pointer1 is not None:
            counter+=1
            if(pointer1==pointer2):
                return pointer1.dataval
            if(counter>diff):
                pointer2=pointer2.nextval
            
            pointer1=pointer1.nextval
    else:
        diff=l2len-l1len
        counter=0
        while pointer2 is not None:
            counter+=1
            if(pointer1==pointer2):
                return pointer1.dataval
            if(counter>diff):
                pointer1=pointer1.nextval
            
            pointer2=pointer2.nextval


list1=[1,2,3]
list2=[4,5,6,7]


Linkedlist1=SLinkedlist()
Linkedlist2=SLinkedlist()

for i in list1:
    Linkedlist1.insertNode(i)
for i in list2:
    Linkedlist2.insertNode(i)
intersectinglist(Linkedlist1,Linkedlist2)
print(detecting(Linkedlist1,Linkedlist2))