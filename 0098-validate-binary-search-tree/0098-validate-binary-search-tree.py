# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        upper, lower = float("inf"), -float("inf")
        def dfs(upper, lower, node):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
                
                
                
            return dfs(node.val, lower, node.left) and dfs(upper, node.val, node.right)
        return dfs(upper, lower, root)