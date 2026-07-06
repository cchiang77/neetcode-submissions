# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        first_iteration = True
        while not (fast is None or fast.next is None):
            if slow is fast and not first_iteration:
                return True
            slow = slow.next
            fast = fast.next.next
            first_iteration = False

        return False