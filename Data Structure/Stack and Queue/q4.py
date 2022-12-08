#Queue via stack: Implement a myqueue class which implements a queue using 2 stack

class Stack:
    def __init__(self) -> None:
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def checkempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.checkempty():
            return
        last=self.stack[-1]
        self.stack.pop()
        return last
    
    def peek(self):
        if(self.stack):
            return self.stack[-1]
        return None
    

class MyQueue:
    def __init__(self) -> None:
        self.Queue=Stack()
        self.oldelement=Stack()

    def pushqueue(self,element):
        self.Queue.push(element)
    
    def popQueue(self):
        if(self.oldelement.checkempty()):
            while(not self.Queue.checkempty()):
                item=self.Queue.pop()
                self.oldelement.push(item)
        return self.oldelement.pop()




l1=MyQueue()
l1.pushqueue(1)
l1.pushqueue(2)
l1.pushqueue(3)
l1.pushqueue(4)
l1.pushqueue(5)
l1.pushqueue(6)
l1.pushqueue(7)
print(l1.popQueue())
print(l1.popQueue())
print(l1.popQueue())
print(l1.popQueue())
print(l1.popQueue())


