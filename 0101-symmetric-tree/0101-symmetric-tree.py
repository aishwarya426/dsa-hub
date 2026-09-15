# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root1:TreeNode|None,root2:TreeNode|None)->bool:
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val!=root2.val:
            return False
        l=self.func(root1.left,root2.right)
        r=self.func(root1.right,root2.left)
        if l==True and r==True:
            return True
        return False
        
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.func(root.left,root.right)
        