class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete=arr[0]
        onedelete=float('-inf')
        ans=arr[0]
        for i in range(1,len(arr)):
            prevnodelete=nodelete
            prevonedelete=onedelete
            nodelete=max(arr[i],nodelete+arr[i])
            if prevonedelete==float("-inf"):
                v2=arr[i]
            else:
                v2=prevonedelete+arr[i]
            onedelete=max(v2,prevnodelete)
            ans=max(ans,max(onedelete,nodelete))
        return ans

        