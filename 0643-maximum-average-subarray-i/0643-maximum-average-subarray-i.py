class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(0,k):
            sum+=nums[i]
        maxsum=sum
        i=0
        j=k-1
        while j+1<=len(nums)-1:
            sum=sum - nums[i] + nums[j+1]
            if  sum> maxsum:
                maxsum=sum
            i+=1
            j+=1

        
        return maxsum/k

            
        