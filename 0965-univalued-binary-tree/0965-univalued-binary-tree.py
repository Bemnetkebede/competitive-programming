# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        if not root:
            return True
        que = deque([root])
        while que:
            for i in range(len(que)):
                node = que.popleft()
                print(node.val , root.val)
                if node.val != root.val:
                    print(node.val , root.val)
                    return False
                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
                
        return True
            

      
