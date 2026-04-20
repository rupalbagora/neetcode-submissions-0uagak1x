# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None : 
            return
        
        p1 = head
        p2 = head

        while p2.next!=None and p2.next.next!=None:
            p1 = p1.next
            p2 = p2.next.next
        
        #Reverse the half after middle
        preMiddle = p1
        preCurrent = p1.next

        while preCurrent.next!=None :
            current = preCurrent.next;
            preCurrent.next=current.next
            current.next=preMiddle.next
            preMiddle.next=current
        
        #start reordering
        p1 =head
        p2=preMiddle.next
        while p1!=preMiddle : 
            preMiddle.next = p2.next
            p2.next=p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMiddle.next
