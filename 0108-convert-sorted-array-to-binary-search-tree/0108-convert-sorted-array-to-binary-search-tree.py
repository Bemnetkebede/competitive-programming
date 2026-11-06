# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
            def helper(nums):
                if not nums:
                    return None
                md = len(nums)//2
                lt = helper(nums[:md])
                rt = helper(nums[md+1:])
                return TreeNode(nums[md] , lt , rt)
            return helper(nums)
            
            


            
        