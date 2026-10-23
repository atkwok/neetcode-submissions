# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return helper(root)[0]

def helper(root: Optional[TreeNode]) -> (bool, int):
    # return if valid, plus min and max value of subtree
    if root.left is None and root.right is None:
        return True, root.val, root.val
    
    max_left = -math.inf
    min_left = None
    if root.left:
        valid_left, min_left, max_left = helper(root.left)
        if not valid_left or max_left >= root.val:
            return False, math.inf, -math.inf
    else:
        min_left = root.val

    min_right = math.inf
    max_right = None
    if root.right:
        valid_right, min_right, max_right = helper(root.right)
        if not valid_right or min_right <= root.val:
            return False, math.inf, -math.inf
    else:
        max_right = root.val
    
    return True, min_left, max_right

        
            
        

        