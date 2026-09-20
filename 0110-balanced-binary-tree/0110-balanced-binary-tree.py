# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=True
    def func(self, root: TreeNode | None)->int:
        if root==None:
            return 0
        left=self.func(root.left)
        right=self.func(root.right)
        if abs(left-right)>1:
            self.ans=False
        return 1+max(left,right)
        
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.ans=True
        self.func(root)
        if self.ans==True:
            return True
        else:
            return False

        
        