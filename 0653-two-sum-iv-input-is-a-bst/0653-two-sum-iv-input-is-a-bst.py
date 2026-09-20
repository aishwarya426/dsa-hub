# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a=[]
    def func(self,root:Optional[TreeNode])->None:
        if root==None:
            return
        self.func(root.left)
        self.a.append(root.val)
        self.func(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.a=[]
        self.func(root)
        i=0
        j=len(self.a)-1
        while i<j:
            if self.a[i]+self.a[j]==k:
                return True
            elif self.a[i]+self.a[j]<k:
                i+=1
            elif self.a[i]+self.a[j]>k:
                j-=1
        return False
        