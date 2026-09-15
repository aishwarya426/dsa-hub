# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,p:TreeNode |None, q:TreeNode |None)->bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val!=q.val:
            return False
        l=self.func(p.left,q.left)
        r=self.func(p.right,q.right)
        if l==True and r==True:
            return True
        return False

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.func(p,q)
        
         
        