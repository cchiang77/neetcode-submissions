class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        levels = []
        stack = [ (root, 0) ]
        while stack:
            root, level_num = stack.pop()

            if len(levels) == level_num:
                levels.append([root.val])
            else:
                levels[level_num].append(root.val)
            
            if root.right:
                stack.append((root.right, level_num + 1))
            
            if root.left:
                stack.append((root.left, level_num + 1))
        
        return levels