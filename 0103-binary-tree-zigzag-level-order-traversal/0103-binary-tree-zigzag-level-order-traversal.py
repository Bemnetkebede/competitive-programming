# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        li = defaultdict(list)
        def helper(root ,row):
            if not root:
                return []
            li[row].append(root.val)
            helper(root.left , row + 1)
            helper(root.right , row + 1)
            
        helper(root , 0)
        ans  = []
        for key , val in li.items():
            if key % 2 != 0:
                ans.append(list(reversed(val)))
            else:
                ans.append(val)
        return ans