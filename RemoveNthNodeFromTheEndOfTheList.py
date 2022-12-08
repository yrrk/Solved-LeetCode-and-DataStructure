# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        count=0
        pointer=head
        Npointer=dum
        while pointer is not None:
            pointer=pointer.next
            count+=1
            if count>n:
                Npointer=Npointer.next   
        Npointer.next=Npointer.next.next
        return dum.next