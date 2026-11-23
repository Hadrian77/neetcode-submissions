# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodeList = []

        while head:
            nodeList.append(head)
            head = head.next
            
        nodeList.pop(len(nodeList)-n)

        if len(nodeList) == 0:
            return

        for x in nodeList:
            print(x.val)

        for x in range(len(nodeList)):
            if x+1 < len(nodeList):
                nodeList[x].next = nodeList[x+1]
            else:
                nodeList[x].next = None
        
        
        return nodeList[0]