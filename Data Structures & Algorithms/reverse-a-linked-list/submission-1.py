# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        return self.reverse(head,None)

    def reverse(self,current:ListNode, previous:ListNode):

        if current.next == None:
            current.next = previous
            return current
        
        newCurrent = current.next
        current.next = previous

        return self.reverse(newCurrent,current)

        