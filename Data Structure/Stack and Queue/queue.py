class Queue:
    def __init__(self) -> None:
        self.Queue=[]

    def push(self,item):
        self.Queue.append(item)
    
    def checkempty(self):
        return len(self.Queue)==0
    
    def pop(self):
        if(self.checkempty()):
            return None
        first=self.Queue[0]
        self.Queue(0)
        return first
    
