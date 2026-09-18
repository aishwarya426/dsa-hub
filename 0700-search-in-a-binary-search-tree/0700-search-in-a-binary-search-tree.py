# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=None
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root==None:
            return root
        if val<root.val:
            self.searchBST(root.left,val)
        if val>root.val:
            self.searchBST(root.right,val)
        if root.val==val:
            self.ans=root

        return self.ans
        
        
        