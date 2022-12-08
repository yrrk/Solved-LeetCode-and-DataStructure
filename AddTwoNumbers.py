# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def addNode(self,data):
        newNode=ListNode(data)
        if(self.val==None):
            self.val=data
            return
        pointer=self
        while pointer.next is not None:
            pointer=pointer.next
        pointer.next=newNode
    

    
def addPadding(list1,list2):
    while list1!=None or list2!=None:
        newNode=ListNode(0)
        if list1.next==None and list2.next==None:
            return
        if list1.next==None:
            list1.next=newNode
        elif list2.next==None:
            list2.next=newNode
        list1=list1.next
        list2=list2.next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addPadding(l1,l2)
        pointer1=l1
        pointer2=l2
        Solution=ListNode()
        lastNode=False
        carry=0
        while pointer1 is not None:
            res=pointer1.val+pointer2.val+carry
            if len(str(res))>1:
                if(pointer1.next==None and pointer2.next==None):
                    lastNode=True
                carry=res//10
                res=res%10
            else:
                carry=0
            Solution.addNode(res)
            pointer1=pointer1.next
            pointer2=pointer2.next
        if lastNode:
            Solution.addNode(carry)
        
        return Solution