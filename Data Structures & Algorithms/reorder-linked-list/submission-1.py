# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first find the middle of the linkedlist and split the linked list there
        slowPtr = head
        fastPtr = head

        if slowPtr.next == None:
            return

        while (slowPtr != None and fastPtr != None and fastPtr.next != None):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        # split the linked lists there
        dummyIter = head
        while (dummyIter.next != slowPtr):
            dummyIter = dummyIter.next
        dummyIter.next = None

        dummy1 = head

        # reverse the second linked list before assigning dummy2 to the head
        prev = None
        curr = slowPtr

        while (curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        dummy2 = prev

        # build out the new linked list using dummy 1 and dummy 2
        while dummy1 != None and dummy1.next != None and dummy2 != None:
            temp = dummy1.next
            temp2 = dummy2.next

            dummy1.next = dummy2
            dummy2.next = temp

            dummy1 = dummy1.next.next
            dummy2 = temp2

        
        if dummy2 != None:
            dummy1.next = dummy2

            


        




