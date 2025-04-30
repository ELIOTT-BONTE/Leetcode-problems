# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        floor, ceiling = -float("inf"), float("inf")
        def dfs(floor, ceiling, node):
            if not node:
                return True
            elif not floor < node.val < ceiling:
                return False
            else:
                return dfs(floor, node.val, node.left) and dfs(node.val, ceiling, node.right)
        
        return dfs(floor, ceiling, root)
        