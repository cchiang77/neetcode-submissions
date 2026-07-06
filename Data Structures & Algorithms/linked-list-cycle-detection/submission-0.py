# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        first_visiting = True

        while not (fast is None or fast.next is None):
            if slow is fast and not first_visiting:
                return True
            
            slow = slow.next
            fast = fast.next.next

            first_visiting = False
        
        return False