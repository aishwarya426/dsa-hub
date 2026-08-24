class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew=s.lower()
        i=0
        j=len(snew)-1
        while i<=j:
            if not (snew[i].isalnum()):
                i+=1
            elif not (snew[j].isalnum()):
                j-=1
            elif snew[i]==snew[j]:
                i+=1
                j-=1
            elif snew[i]!=snew[j]:
                return False
        return True
        