import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict= collections.defaultdict(list)
        for s in strs:
            freq=[0]*26
            for ch in s:
                freq[ord(ch)-ord('a')]+=1
            mydict[tuple(freq)].append(s)
        return list(mydict.values())

        