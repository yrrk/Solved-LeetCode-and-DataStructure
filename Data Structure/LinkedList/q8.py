#Loop Detection:Given a circular list implement an algorithm that return the node at the beginning of the node
#Definition
#Circular LinkedList: A corrupt linked list in which a node's next pointer points to an earlier node, So as to make a loop in 
#the linked list
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


def findbegin(list1):
    hashtable={}
    pointer1=list1.headval
    counter=0
    while pointer1 is not None:
        counter+=1
        if(pointer1 in hashtable.values()):
            return pointer1.dataval
        else:
            hashtable[counter]=pointer1
        pointer1=pointer1.nextval

Head=SLinkedlist()
Head.headval=Node(1)
Node1=Node(2)
Head.headval.nextval=Node1
Node2=Node(3)
Node1.nextval=Node2
Node3=Node(4)
Node2.nextval=Node3
Node4=Node(5)
Node3.nextval=Node4
Node4.nextval=Node2

print(findbegin(Head))