# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = defaultdict(lambda :float('-inf'))
        def helper(root , level):
            if not root:
                return
            arr[level] = max(root.val,arr[level])
            helper(root.left, level+1)
            helper(root.right , level +1)
            
        helper(root,0)
        ans = []
        for i,v in arr.items():
            ans.append(v)
        return ans

        