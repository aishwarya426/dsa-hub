class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
            
        freq = [0]*26
        for ch in s:
            j=ord(ch)-ord('a')
            freq[j]+=1
        for ch in t:
            j=ord(ch)-ord('a')
            freq[j]-=1
        for x in freq:
            if x!=0:
                return False
                break
        return True
        