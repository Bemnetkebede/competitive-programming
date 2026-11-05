# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def helper(node):
            nonlocal max_sum
            if not node:
                # is BST, min=inf, max=-inf, sum=0
                return True, float('inf'), float('-inf'), 0

            l_isBST, l_min, l_max, l_sum = helper(node.left)
            r_isBST, r_min, r_max, r_sum = helper(node.right)

            # Check if current node forms a BST
            if l_isBST and r_isBST and l_max < node.val < r_min:
                curr_sum = node.val + l_sum + r_sum
                max_sum = max(max_sum, curr_sum)
                curr_min = min(l_min, node.val)
                curr_max = max(r_max, node.val)
                return True, curr_min, curr_max, curr_sum
            else:
                # Not a BST, return False
                return False, 0, 0, 0

        helper(root)
        return max_sum

        