class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        left = {}
        for i, c in enumerate(s):
            if c not in left:
                left[c] = i
        right = {}
        for i, c in enumerate(s):
            right[c] = i

        ans = []
        prev_end = -1
        for i, c in enumerate(s):
            if i != left[c]:
                continue
            end = right[c]
            j = i
            valid = True
            
            while j <= end:
                if left[s[j]] < i:
                    valid = False
                    break
                end = max(end, right[s[j]])
                j += 1
                
            if valid:
                if i <= prev_end:
                    ans[-1] = s[i:end+1]
                else:
                    ans.append(s[i:end+1])
                prev_end = end
                
        return ans
