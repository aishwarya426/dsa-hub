# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        res=[]
        queue=deque([root])
        while queue:
            length=len(queue)
            currlevel=[]
            for i in range(length):
                node=queue.popleft()
                currlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(currlevel)
        return res[::-1]
        