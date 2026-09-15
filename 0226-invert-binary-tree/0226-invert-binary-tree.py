# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self,root:TreeNode|None)->TreeNode|None:
        if root==None:
            return root
        if root.left==None and root.right==None:
            return root
        temp=root.left
        root.left=root.right
        root.right=temp
        self.swap(root.left)
        self.swap(root.right)
        return root
        


    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        return self.swap(root)
        