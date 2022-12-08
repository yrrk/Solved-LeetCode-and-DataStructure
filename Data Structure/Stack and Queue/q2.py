#Stack Min: How would you design a stack which in addition to peek and pop has a function min which return min element
#Push, pop and min should all operate in O(1) time


class Stack:
    def __init__(self) -> None:
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)

    def checkempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if(self.checkempty()):
            return None
        item=self.stack[-1]
        self.stack.pop()
        return item
    
    def peek(self):
        if(self.stack):
            return self.stack[-1]
        return None
    
    def min(self):
        mini=self.peek()
        while(not self.checkempty()):
            if(mini<self.peek()):
                pass
            else:
                mini=self.peek()
            self.stack.pop()
        return mini

l1=Stack()
items=[9,16,3,1,11,12,19,10,5,6,7,14,2,17,15,20,18]

for i in items:
    l1.push(i)
print(l1.min())
