# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
       
    
        dummy = Node(0, head)

        # Initialize slow and fast pointers at dummy
        slow = dummy
        fast = dummy

        # Move fast pointer N+1 steps ahead to create a gap
        for _ in range(N + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Slow is now at node before target → delete target node
        slow.next = slow.next.next

        # Return updated head
        return dummy.next

        