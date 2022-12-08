#Stack of Plates: Imagine a (literal) stack of plates. if the stack goes to high, it might topple
#Therefore, in real life, we would likely start a new stack when the prevoius stack exceeds some threshold .
#Implement a DataStructure setofstack that mimics set of stacks
#SetofStacks should be composed of several stack and should create a new stack
#Once the previous stack exceed capacity SetofStack.push() and SetofStack.pop() should behave identically to a single stack
# i.e. pop() should return the same values as it would if there were just a single stack

class SetofStack:
    def __init__(self) -> None:
        self.SetStack=[]
    
    def pushStack(self,list1):
        self.SetStack.append(list1)

    def checkemptyset(self):
        return len(self.SetStack)==0
    
    def popStack(self):
        if(self.checkemptyset()):
            return None
        last=self.SetStack[-1]
        self.SetStack.pop()
        return last
    
    def peekStack(self):
        if(self.SetStack):
            return self.SetStack[-1]
        return None
    

class Stack(SetofStack):
    def __init__(self,thres) -> None:
        super().__init__()
        self.stack=[]
        self.thres=thres

    def push(self,item):
        if(len(self.stack)>=self.thres):
            newStack=Stack(self.thres)
            newStack.push(item)
            self.pushStack(self.stack)
            self.stack=newStack.stack
        else:
            self.stack.append(item)

    def checkempty(self):
        return len(self.stack)==0


    def pop(self):
        if(self.checkemptyset()):
            return "Stack is empty"
        if(self.checkempty()):
            self.stack=self.popStack()
            last=self.stack[-1]
            self.stack.pop()
            return last
        else:
            last=self.stack[-1]
            self.stack.pop()
            return last
    
    
l1=Stack(3)
items=[9,16,3,1,11,12,19,10,5,6,7,14,2,17,15,20,18]
for i in items:
    l1.push(i)
print(l1.SetStack)
print(l1.stack)
l1.pop()
print(l1.stack)
l1.pop()
print(l1.stack)

l1.pop()
print(l1.SetStack)
print(l1.stack)
