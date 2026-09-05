class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        ans=[0]*len(nums)
        k=len(nums)-1
        while i<=j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                ans[k]=nums[j]*nums[j]
                j-=1
                k-=1
            else:
                ans[k]=nums[i]*nums[i]
                i+=1
                k-=1

        return ans

