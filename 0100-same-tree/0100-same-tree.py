# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        resP = []
        resQ = []
        def dfs(node, res):
            if not node:
                res.append(None)
                return
            dfs(node.left,res)
            dfs(node.right,res)
            res.append(node.val)
        dfs(p, resP)
        dfs(q, resQ)

        return resP == resQ