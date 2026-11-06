# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        my_dict = defaultdict(list)
        def helper(root,row):
            if not root:
               return
            my_dict[row].append(root)
            helper(root.left , row+1)
            helper(root.right , row+1)
        helper(root,0)
        my_dict = dict(sorted(my_dict.items()))
        for level, nodes in my_dict.items():
            if level % 2 == 1: 
                values = [node.val for node in nodes]
                values.reverse()
                for i, node in enumerate(nodes):
                    node.val = values[i]
        return root


            
        