# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1
        head2 = list2

        dummy = ListNode()
        iter1 = dummy

        while (head1 != None and head2 != None):
            if head1.val <= head2.val:
                iter1.next = head1
                head1 = head1.next
                iter1 = iter1.next
            else:
                iter1.next = head2
                head2 = head2.next
                iter1 = iter1.next

        if head1 != None:
            while (head1 != None):
                iter1.next = head1
                head1 = head1.next
                iter1 = iter1.next

        elif head2 != None:
            while (head2 != None):
                iter1.next = head2
                head2 = head2.next
                iter1 = iter1.next


        return dummy.next
        