# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=deque([root])
        res=[]
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
            length=len(queue)
            currlevel=[]
            for i in range(length):
                node=queue.popleft()
                currlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(currlevel)!=0:
                res.append(currlevel[::-1])
        return res


        