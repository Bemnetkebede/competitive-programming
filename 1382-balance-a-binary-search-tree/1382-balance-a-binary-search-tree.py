# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            arr.append(root.val)
            helper(root.right)
        helper(root)
        print(arr)
        def func(arr):
            if not arr:
                return
            if len(arr) == 1:
                return TreeNode(arr[0])
            md = len(arr)//2
            left = func(arr[:md])
            right = func(arr[md+1:])
            return TreeNode(arr[md] , left , right)
        return func(arr)


        
            
       

        