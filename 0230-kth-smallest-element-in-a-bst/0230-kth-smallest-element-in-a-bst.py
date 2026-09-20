# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a=[]
    def func(self,root:TreeNode | None)->None:
        if root==None :
            return
        self.func(root.left)
        self.a.append(root.val)
        self.func(root.right)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.a=[]
        self.func(root)
        print(self.a)
        return self.a[k-1]
        

        