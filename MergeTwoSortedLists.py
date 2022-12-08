# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1=list1
        pointer2=list2
        srted=ListNode()
        cur=srted
       
        while pointer1 or pointer2:
            if(pointer1 is None):
                cur.next=ListNode(pointer2.val)
                cur=cur.next
                pointer2=pointer2.next
                continue
            elif(pointer2 is None):
                cur.next=ListNode(pointer1.val)
                cur=cur.next
                pointer1=pointer1.next
                continue
                
            if(pointer1.val<=pointer2.val):
                cur.next=ListNode(pointer1.val)
                cur=cur.next
                pointer1=pointer1.next
                continue
                 
            else:
                cur.next=ListNode(pointer2.val)
                cur=cur.next
                pointer2=pointer2.next
                continue
            # cur=cur.next
            # pointer1=pointer1.next
            # pointer2=pointer2.next
        srted=srted.next
        return srted
        