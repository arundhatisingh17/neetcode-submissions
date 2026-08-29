# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # first get the length of the linked list
        l = 0
        iter1 = head
        iter2 = head

        while (iter1 != None):
            l += 1
            iter1 = iter1.next

        if l == 1 and n == 1:
            return None

        target = l - n
        if target == 0:
            rem = head
            temp = rem.next
            rem.next = None
            head = temp

        cntr = 0

        while (iter2 != None):
            if cntr == target - 1:
                iter2.next = iter2.next.next
            cntr += 1
            iter2 = iter2.next

        return head
