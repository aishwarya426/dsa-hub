# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root:Optional[TreeNode], res:List[int])->None:
        
        if root==None:
            return 
        self.func(root.left,res)
        res.append(root.val)
        self.func(root.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.func(root,res)
        return res
        