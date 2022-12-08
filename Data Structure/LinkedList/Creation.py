class Node:
    def __init__(self,dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None


class Slinkedlist:
    def __init__(self) -> None:
        self.headval=None



headNode=Slinkedlist()
headNode.headval=Node("Mon")
Node2=Node("Tue")
Node3=Node("Wed")
Node4=Node("Thur")
headNode.headval.nextval=Node2
Node2.nextval=Node3
Node3.nextval=Node4

