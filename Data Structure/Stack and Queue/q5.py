#Sort Stack: Write a program to sort a stack such that the smallest items are on the top
#You can use an additional temporary stack, but you may not copy element into any other data structure(such as an array)
#The stack supports the following operations: push, pop, peek and isEmpty


class Stack:
    def __init__(self) -> None:
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
    
    def checkempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if(self.checkempty()):
            return
        last=self.stack[-1]
        self.stack.pop()
        return last
    
    def peek(self):
        if(self.stack):
            return self.stack[-1]
        return 
    

def sortstack(stack1):
    spare=Stack()
    spare.push(stack1.pop())
    while(not stack1.checkempty()):
        if(stack1.peek()>spare.peek()):
            temp=stack1.pop()
            while(temp>spare.peek()):
                stack1.push(spare.pop())
                if(spare.checkempty()):
                    break
            spare.push(temp)
        else:
            spare.push(stack1.pop())
    print(spare.stack)



l1=Stack()
l1.push(7)
l1.push(1)
l1.push(4)
l1.push(3)
l1.push(6)
l1.push(2)
l1.push(5)

sortstack(l1)

