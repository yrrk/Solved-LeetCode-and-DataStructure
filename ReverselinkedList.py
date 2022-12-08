# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def insertnodeatstart(linky,data):
    newNode=ListNode(data)
    # if(linky.val==0):
    #     linky.val=data
    newNode.next=linky
    return newNode
            
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return None
        pointer=head.next
        revlist=ListNode(head.val)
        while(pointer is not None):
            revlist=insertnodeatstart(revlist,pointer.val)
            pointer=pointer.next
        return revlist