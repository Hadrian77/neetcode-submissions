# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        return self.mergeK(0,len(lists)-1,lists)
        
    
    def mergeK(self,start:int,end:int,lists: List[Optional[ListNode]]):
        if (end - start) == 0:
            return lists[start]

        mid = (end + start) //2
        
        left = self.mergeK(start,mid,lists)

        right = self.mergeK(mid+1,end,lists)

        return self.merge(left,right)





    def merge(self,first:[ListNode], second: [ListNode]):

        if not first or not second:
            if first:
                return first
            
            if second:
                return second

        if first.val <= second.val:
            result = first
            current = first

        else:
            result = second
            current = second

        while first and second:

            if first.val <= second.val:
                save = first
                first = first.next
                current.next = save
            
            else:
                save = second
                second = second.next
                current.next = save
                
            current = current.next
        
        if first:
            current.next = first
        if second:
            current.next = second


        return result