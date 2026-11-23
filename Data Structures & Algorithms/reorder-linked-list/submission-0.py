# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        last = self.findEnd(head)

        while last and head:
            saveLast = last.next
            saveHead = head.next

            head.next = last
            last.next = saveHead

            head = saveHead
            last = saveLast
        
        return head





    def findEnd(self,head):

        last  = head
        mid = head
        

        while last.next:
            if last.next.next:
                last = last.next.next
            else:
                last = last.next
                break
            
            mid = mid.next
        
        prev = None

        while mid:
            save = mid.next
            mid.next = prev
            prev = mid
            mid = save

        return (last)