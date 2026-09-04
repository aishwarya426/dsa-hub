class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        f=1
        while f<len(nums):
            if nums[s]==nums[f]:
                f+=1
            else:
                nums[s+1]=nums[f]
                s+=1
                f+=1
        return s+1

            
       