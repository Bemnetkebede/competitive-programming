# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        g_max = 0
        def helper(root , min_val , max_val):
            nonlocal g_max
            if not root:
                return 
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            g_max = max(g_max, abs(max_val - min_val))
            helper(root.left, min_val, max_val)
            helper(root.right, min_val, max_val)


        helper(root, root.val, root.val)
        return g_max



        

        