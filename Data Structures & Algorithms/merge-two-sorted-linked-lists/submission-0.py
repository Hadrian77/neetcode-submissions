# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2

        if not list2:
            return list1

        head : ListNode
        last : ListNode

        if list1.val < list2.val:
            head = list1
            last = head
            list1 = list1.next
        else:
            head = list2
            last = head
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                last = list1
                list1 = list1.next
            else:
                last.next = list2
                last = list2
                list2 = list2.next

        if not list1:
            last.next = list2
        else:
            last.next = list1
            
        return head
            