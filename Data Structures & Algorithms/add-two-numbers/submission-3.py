# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = False
        ansList = ListNode()
        curr = ansList

        while (l1 != None and l2 != None):
            temp_sum = l1.val + l2.val
            if carry:
                temp_sum += 1
                carry = False

            if temp_sum >= 10:
                carry = True

            node = ListNode(temp_sum % 10)
            curr.next = node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        if l1 != None:
            while l1 != None:
                temp_sum = l1.val
                if carry:
                    temp_sum += 1
                    carry = False

                if temp_sum >= 10:
                    carry = True

                node = ListNode(temp_sum % 10)
                curr.next = node
                curr = curr.next
                l1 = l1.next

        elif l2 != None:
            while l2 != None:
                temp_sum = l2.val
                if carry:
                    temp_sum += 1
                    carry = False

                if temp_sum >= 10:
                    carry = True

                node = ListNode(temp_sum % 10)
                curr.next = node
                curr = curr.next
                l2 = l2.next

        if carry:
            node = ListNode(1)
            curr.next = node

        return ansList.next

