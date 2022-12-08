#Implementation of stack
class Stack:
    def __init__(self) -> None:
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
    
    def checkempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if(self.checkempty()):
            print("Stack is empty")
            return
        self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

S1=Stack()
S1.push(1)
S1.push(2)
S1.push(3)
print(S1.stack)
S1.pop()
S1.pop()
S1.pop()
S1.pop()