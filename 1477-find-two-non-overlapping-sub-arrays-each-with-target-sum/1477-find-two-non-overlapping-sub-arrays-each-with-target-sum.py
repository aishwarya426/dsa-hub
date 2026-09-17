class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        best = [float('inf')] * (len(arr) + 1)
        left, curr_sum, ans = 0, 0, float('inf')
    
        for right, val in enumerate(arr):
            curr_sum += val
        
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            best[right + 1] = best[right]
        
            if curr_sum == target:
                length = right - left + 1
                ans = min(ans, length + best[left])
                best[right + 1] = min(best[right], length)
            
        if ans != float('inf'):
            return ans
        else:
            return -1
            


        