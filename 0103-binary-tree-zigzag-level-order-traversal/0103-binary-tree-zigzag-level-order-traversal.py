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
        flag=0
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
            if flag==0:
                res.append(currlevel)
            else:
                res.append(currlevel[::-1])
            flag=not flag
            
        return res


        