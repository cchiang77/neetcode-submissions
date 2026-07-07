class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val1, val2 = p.val, q.val
        path1 = find_path(root, val1)
        path2 = find_path(root, val2)
        set2 = {node.val for node in path2}
        
        for node in path1:
            if node.val in set2:
                return node

def find_path(root, target_val):
  if root is None:
    return None
  
  if root.val == target_val:
    return [ root ]
  
  left_path = find_path(root.left, target_val)
  if left_path is not None:
    left_path.append(root)
    return left_path
  
  right_path = find_path(root.right, target_val)
  if right_path is not None:
    right_path.append(root)
    return right_path
  
  return None