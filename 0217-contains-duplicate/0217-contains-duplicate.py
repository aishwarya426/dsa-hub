class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        isin = set()
        for i in range (len(nums)):
            if nums[i] in isin:
                return True
            else:
                isin.add(nums[i])
        return False  