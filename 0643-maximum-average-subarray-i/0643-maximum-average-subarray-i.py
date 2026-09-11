class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        n=len(nums)
        for i in range(0,k):
            sum+=nums[i]
        res=sum
        l=0
        h=k-1
        while h<n:
            res=max(res,sum)
            if h+1==n:
                break
            sum=sum-nums[l]+nums[h+1]
            l+=1
            h+=1
        return res/k
        

            
        