# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        pntr1 = head
        pntr2 = head

        while (pntr1 != None and pntr2 != None and pntr2.next != None):
            pntr1 = pntr1.next
            pntr2 = pntr2.next.next

            if pntr1 == pntr2:
                return True

        return False
