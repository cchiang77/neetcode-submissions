# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.lst = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.lst.append(node.val)
            self.cnt += 1
            if self.cnt == k:
                return
            traverse(node.right)
        
        traverse(root)
        return self.lst[k-1]