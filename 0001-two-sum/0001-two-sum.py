class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        store={}
        for i,x in enumerate(nums):
            store[x]=i
        for i in range(len(nums)):
            need=target - nums[i]
            if need in store and store[need]!=i:
                ans.append(i)
                ans.append(store[need])
                break
        return ans
            

                
        