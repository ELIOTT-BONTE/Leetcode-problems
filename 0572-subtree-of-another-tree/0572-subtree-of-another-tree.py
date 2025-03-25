# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        #function to determine if trees are identical
        def is_same(tree1,tree2):
            if not tree1 and not tree2:
                return True
            elif not tree1 or not tree2:
                return False
            else:
                return tree1.val == tree2.val and is_same(tree1.left, tree2.left) and is_same(tree1.right, tree2.right)


            #call function identical on each node, in dfs manner
        def dfs(node, target):
            if not node:
                return False
            elif is_same(node, target):
                return True
            
            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, subRoot)