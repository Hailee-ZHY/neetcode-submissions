# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = set()
        curr = head
        
        while curr:
            if not curr.next:
                return False 
            
            elif curr.val in cache:
                return True 
            
            else:
                cache.add(curr.val)
                curr = curr.next

        return False