# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans=None

    def func(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if root==None:
            return 0
        left=self.func(root.left,p,q)
        right=self.func(root.right,p,q)
        s=0
        if root==p or root==q:
            s=1
        total=left+right+s
        if total==2 and self.ans==None:
            self.ans=root
        return total
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.func(root,p,q)
        return self.ans
        
        