# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        current.next = ListNode()
        carry = 0
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0



        while v1 or v2 or carry:
            
            
            value = v1 + v2 + carry

            if value > 9:
                carry = 1
                value -= 10
            else:
                carry = 0    
            
            current.next = ListNode(value)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0


        return dummy.next




        