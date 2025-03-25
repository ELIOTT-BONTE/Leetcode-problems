# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #root is middle
        #left and right children are roots are subarrays
        #recur it

        def BST(array):
            if not array:
                return None
            middle = TreeNode()
            mid = (len(array)-1)//2
            middle.val = array[(len(array)-1)//2]
            middle.left = BST(array[:mid])
            middle.right = BST(array[mid+1:])
            return middle
        return BST(nums)